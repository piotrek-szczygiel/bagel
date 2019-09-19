from PySide2.QtCore import QRegExp, Qt, Signal
from PySide2.QtGui import QIntValidator, QPixmap, QRegExpValidator
from PySide2.QtWidgets import QMessageBox, QWidget

import utils
from ctx import ctx
from ui.add_contractor import Ui_AddContractor


class AddContractor(QWidget):
    finished = Signal()

    def __init__(self, parent=None) -> None:
        super(AddContractor, self).__init__(parent)
        self.ui = Ui_AddContractor()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Widget)

        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("add_contractor.png")))

        self.ui.input_zip_1.setValidator(QIntValidator(0, 99))
        self.ui.input_zip_2.setValidator(QIntValidator(0, 999))
        self.ui.input_zip_1.textEdited.connect(self.skip_zip_1)
        self.ui.input_zip_2.textEdited.connect(self.skip_zip_2)

        self.ui.input_nip.setValidator(QRegExpValidator(QRegExp("[0-9]*")))
        self.ui.input_nip.textEdited.connect(self.validate_nip)

        self.ui.input_regon.setValidator(QRegExpValidator(QRegExp("[0-9]*")))
        self.ui.input_regon.textEdited.connect(self.validate_regon)

        self.valid_pixmap = QPixmap(ctx.resource("valid.png"))
        self.invalid_pixmap = QPixmap(ctx.resource("invalid.png"))

        self.ui.button_add.clicked.connect(self.add_contractor)
        self.ui.button_cancel.clicked.connect(self.ask_close)

    def ask_close(self) -> None:
        answer = QMessageBox.question(
            self,
            "Potwierdź anulowanie",
            "Czy na pewno chcesz anulować dodawanie kontrahenta?",
        )

        if answer == QMessageBox.Yes:
            self.finished.emit()

    def validate_nip(self) -> None:
        nip_str = self.ui.input_nip.text()
        if len(nip_str) != 10:
            return

        nip = [int(c) for c in nip_str]
        if utils.validate_nip(nip):
            self.ui.label_nip_valid.setPixmap(self.valid_pixmap)
            self.ui.label_nip_valid.setToolTip("NIP jest prawidłowy")
        else:
            self.ui.label_nip_valid.setPixmap(self.invalid_pixmap)
            self.ui.label_nip_valid.setToolTip("NIP nie jest prawidłowy")

    def validate_regon(self) -> None:
        regon_str = self.ui.input_regon.text()
        if len(regon_str) != 9:
            return

        regon = [int(c) for c in regon_str]
        if utils.validate_regon(regon):
            self.ui.label_regon_valid.setPixmap(self.valid_pixmap)
            self.ui.label_regon_valid.setToolTip("REGON jest prawidłowy")
        else:
            self.ui.label_regon_valid.setPixmap(self.invalid_pixmap)
            self.ui.label_regon_valid.setToolTip("REGON nit jest prawidłowy")

    def skip_zip_1(self) -> None:
        if len(self.ui.input_zip_1.text()) == 2:
            self.ui.input_zip_2.setFocus()

    def skip_zip_2(self) -> None:
        if len(self.ui.input_zip_2.text()) == 3:
            self.ui.input_city.setFocus()

    def add_contractor(self) -> None:
        first_name = self.ui.input_first_name.text()
        last_name = self.ui.input_last_name.text()
        zip_code = self.ui.input_zip_1.text() + self.ui.input_zip_2.text()
        city = self.ui.input_city.text()
        street = self.ui.input_street.text()
        company_name = self.ui.input_company.text()
        nip = self.ui.input_nip.text()
        regon = self.ui.input_regon.text()

        errors = ""

        if not first_name:
            errors += "Proszę wprowadzić imię kontrahenta.\n"

        if not last_name:
            errors += "Proszę wprowadzić nazwisko kontrahenta.\n"

        if len(zip_code) != 5:
            errors += "Proszę wprowadzić prawidłowy kod pocztowy.\n"

        if not city:
            errors += "Proszę wprowadzić miasto.\n"

        if not street:
            errors += "Proszę wprowadzić ulicę i numer\n"

        if not company_name:
            errors += "Proszę wprowadzić nazwę firmy.\n"

        if not utils.validate_nip([int(c) for c in nip]):
            errors += "Proszę wprowadzić prawidłowy NIP.\n"

        if not regon:
            regon = None
        elif not utils.validate_regon([int(c) for c in regon]):
            errors += "Proszę wprowadzić prawidłowy REGON.\n"

        if errors:
            errors = errors
            QMessageBox.critical(self, "Błąd dodawania kontrahenta", errors)
            return

        c = ctx.db.cursor()

        try:
            c.execute(
                r"""
                INSERT INTO contractors (
                    first_name, last_name, zip_code, city,
                    street, company_name, nip, regon
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    first_name,
                    last_name,
                    zip_code,
                    city,
                    street,
                    company_name,
                    nip,
                    regon,
                ),
            )
        except Exception as e:
            QMessageBox.critical(self, "Błąd bazy danych", str(e))
        else:
            ctx.db.commit()
            QMessageBox.information(
                self, "Sukces", "Pomyślnie dodano nowego kontrahenta."
            )
            self.finished.emit()

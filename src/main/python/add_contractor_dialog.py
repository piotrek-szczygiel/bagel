from PySide2.QtCore import QRegExp
from PySide2.QtGui import QIntValidator, QPixmap, QRegExpValidator
from PySide2.QtWidgets import QDialog

import utils
from ctx import ctx
from ui.add_contractor_dialog import Ui_AddContractorDialog


class AddContractorDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(AddContractorDialog, self).__init__(parent)
        self.ui = Ui_AddContractorDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(
            QPixmap(ctx.resource("add_contractor.png"))
        )
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

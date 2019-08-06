import sqlite3
from hashlib import sha512

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from ctx import ctx
from ui.add_user import Ui_AddUser


class AddUser(QWidget):
    finished = Signal(bool)

    def __init__(self, parent=None) -> None:
        super(AddUser, self).__init__(parent)
        self.ui = Ui_AddUser()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Widget)
        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("add_user.png")))
        self.ui.input_confirm.textChanged.connect(self.check_passwords)
        self.ui.input_password.textChanged.connect(self.check_passwords)
        self.ui.input_confirm.returnPressed.connect(self.add_user)
        self.ui.button_add_user.clicked.connect(self.add_user)
        self.ui.button_cancel.clicked.connect(self.ask_close)

    def ask_close(self) -> None:
        answer = QMessageBox.question(
            self,
            "Potwierdź anulowanie",
            "Czy na pewno chcesz anulować dodawanie użytkownika?",
        )

        if answer == QMessageBox.Yes:
            self.finished.emit(False)

    def check_passwords(self) -> None:
        password = self.ui.input_password.text()
        confirm = self.ui.input_confirm.text()

        if not confirm:
            return

        if password != confirm:
            self.ui.input_confirm.setStyleSheet("border: 2px solid red")
        else:
            self.ui.input_confirm.setStyleSheet("border: 1px solid black")

    def add_user(self) -> None:
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()
        confirm = self.ui.input_confirm.text()
        admin = self.ui.combo_type.currentIndex()

        errors = ""

        if not login:
            errors += "Proszę wprowadzić nazwę użytkownika!\n"

        if len(password) < 6:
            errors += "Hasło nie może być krótsze niż 6 znaków!\n"

        if password != confirm:
            errors += "Hasła się nie zgadzają!\n"

        if errors:
            errors = errors.strip()
            QMessageBox.critical(self, "Błąd dodawania użytkownika", errors)
            return

        hash_password = sha512(password.encode()).hexdigest()

        c = ctx.db.cursor()

        try:
            c.execute(
                r"""
                INSERT INTO users (login, password, admin)
                VALUES (?, ?, ?)
                """,
                (login, hash_password, admin),
            )
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(
                self, "Błąd", f"Użytkownik o loginie {login} już istnieje!\n\n{str(e)}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Błąd bazy danych", str(e))
        else:
            ctx.db.commit()
            QMessageBox.information(
                self, "Sukces", "Pomyślnie dodano nowego użytkownika."
            )
            self.finished.emit(True)

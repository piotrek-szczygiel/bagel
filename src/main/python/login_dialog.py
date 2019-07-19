from hashlib import sha512

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QMessageBox

from ctx import ctx
from ui.login_dialog import Ui_LoginDialog


class LoginDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("lock.png")))
        self.ui.button_login.clicked.connect(self.login)
        self.setWindowFlags(
            (self.windowFlags() | Qt.CustomizeWindowHint)
            & ~Qt.WindowCloseButtonHint
        )

    def login(self) -> None:
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()

        hash_password = sha512(password.encode()).hexdigest()

        c = ctx.db.cursor()
        c.execute(
            "select * from users where login=? and password=?",
            (login, hash_password),
        )

        if c.fetchone() is None:
            QMessageBox.critical(
                self,
                "Błąd logowania",
                "Niepoprawna nazwa użytkownika lub hasło!",
            )
            self.ui.input_password.clear()
            ctx.login = ""
        else:
            ctx.login = login
            self.accept()

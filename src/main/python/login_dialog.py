from hashlib import sha512

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
        self.ui.button_cancel.clicked.connect(self.close)

    def login(self) -> None:
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()

        hash_password = sha512(password.encode()).hexdigest()

        c = ctx.db.cursor()
        c.execute(
            "select * from users where login=? and password=?",
            (login, hash_password),
        )

        user = c.fetchone()

        if user is None:
            QMessageBox.critical(
                self,
                "Błąd logowania",
                "Niepoprawna nazwa użytkownika lub hasło!",
            )
            self.ui.input_password.clear()
            ctx.login = ""
        else:
            ctx.login = login
            ctx.admin = user[3] == 1

            ctx.main.main_window.ui.actionAddUser.setEnabled(ctx.admin)
            ctx.main.main_window.ui.actionDeleteUser.setEnabled(ctx.admin)

            self.accept()

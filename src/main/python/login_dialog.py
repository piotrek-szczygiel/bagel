from hashlib import sha512

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QDialog, QLineEdit, QMessageBox

from ctx import ctx
from ui.login_dialog import Ui_LoginDialog


class LoginDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("lock.png")))
        self.ui.input_login.addAction(
            QIcon(ctx.resource("login.png")), QLineEdit.LeadingPosition
        )
        self.ui.input_password.addAction(
            QIcon(ctx.resource("password.png")), QLineEdit.LeadingPosition
        )
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

            ctx.main.main_window.ui.action_add_user.setEnabled(ctx.admin)
            ctx.main.main_window.ui.action_delete_user.setEnabled(ctx.admin)
            ctx.main.main_window.ui.action_add_contractor.setEnabled(ctx.admin)

            self.accept()

from hashlib import sha512

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QLineEdit, QMessageBox, QWidget

from ctx import ctx
from ui.login import Ui_Login


class Login(QWidget):
    finished = Signal()

    def __init__(self, parent=None) -> None:
        super(Login, self).__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Widget)
        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("lock.png")))
        self.ui.input_login.addAction(
            QIcon(ctx.resource("login.png")), QLineEdit.LeadingPosition
        )
        self.ui.input_password.addAction(
            QIcon(ctx.resource("password.png")), QLineEdit.LeadingPosition
        )
        self.ui.input_password.returnPressed.connect(self.login)
        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_cancel.clicked.connect(self.close)

    def login(self) -> None:
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()

        hash_password = sha512(password.encode()).hexdigest()

        c = ctx.db.cursor()
        c.execute(
            "select * from users where login=? and password=?", (login, hash_password)
        )

        user = c.fetchone()

        if user is None:
            QMessageBox.critical(
                self, "Błąd logowania", "Niepoprawna nazwa użytkownika lub hasło!"
            )
            self.ui.input_password.clear()
            ctx.login = ""
        else:
            ctx.logged_in = True
            ctx.login = login
            ctx.admin = user[3] == 1

            self.finished.emit()

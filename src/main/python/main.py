from fbs_runtime.application_context.PySide2 import ApplicationContext
from ui.main_window import Ui_MainWindow
from ui.login_dialog import Ui_LoginDialog
from PySide2.QtWidgets import QMainWindow, QDialog
from PySide2.QtGui import QPixmap

import sys

ctx = ApplicationContext()


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(QPixmap(ctx.get_resource("lock.png")))
        self.ui.button_login.clicked.connect(self.login)

    def login(self):
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()

        print(f"{login}:{password}")
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.close)

        self.ui.listWidget_sellers.addItem("Test 1")
        self.ui.listWidget_sellers.addItem("Test 2")

        self.login_form = LoginDialog(self)
        self.login_form.show()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.show()

    exit_code = ctx.app.exec_()
    sys.exit(exit_code)

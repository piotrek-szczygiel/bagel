import os
import subprocess

from PySide2.QtWidgets import QMainWindow, QMessageBox

from add_user_dialog import AddUserDialog
from ctx import ctx
from delete_user_dialog import DeleteUserDialog
from login_dialog import LoginDialog
from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, db_path) -> None:
        super(MainWindow, self).__init__()

        self.db_path = db_path

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionOpenDir.triggered.connect(self.open_dir)

        self.ui.actionAddUser.triggered.connect(self.add_user)
        self.ui.actionDeleteUser.triggered.connect(self.delete_user)
        self.ui.actionLogout.triggered.connect(self.logout)

    def open_dir(self) -> None:
        if os.name == "nt":
            cmd = f'explorer /select,"{self.db_path}"'
            subprocess.Popen(cmd)

    def add_user(self) -> None:
        if not ctx.admin:
            return

        add_user_dialog = AddUserDialog(self)
        add_user_dialog.accepted.connect(self.login)
        add_user_dialog.open()

    def delete_user(self) -> None:
        if not ctx.admin:
            return

        delete_user_dialog = DeleteUserDialog(self)
        delete_user_dialog.open()

    def login(self) -> None:
        if ctx.login:
            return

        self.hide()
        login_dialog = LoginDialog(self)
        login_dialog.accepted.connect(self.logged_in)
        login_dialog.open()

    def logged_in(self) -> None:
        if not ctx.login:
            return

        self.setWindowTitle(
            "Bagel v0.1.0 - " + ctx.login + " (Administrator)"
            if ctx.admin
            else ""
        )

        self.show()

    def logout(self, ask=True) -> None:
        if ask:
            answer = QMessageBox.question(
                self,
                "Potwierdzenie wylogowania",
                "Czy na pewno chcesz się wylogować?",
            )

            if answer == QMessageBox.No:
                return

        ctx.login = ""

        self.login()

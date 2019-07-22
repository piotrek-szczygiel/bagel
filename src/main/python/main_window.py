import os
import subprocess

from PySide2.QtWidgets import QMainWindow, QMessageBox

from add_contractor_dialog import AddContractorDialog
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

        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_open_dir.triggered.connect(self.open_dir)

        self.ui.action_add_user.triggered.connect(self.add_user)
        self.ui.action_delete_user.triggered.connect(self.delete_user)
        self.ui.action_logout.triggered.connect(self.logout)

        self.ui.action_add_contractor.triggered.connect(self.add_contractor)

    def open_dir(self) -> None:
        if os.name == "nt":
            cmd = f'explorer /select,"{self.db_path}"'
            subprocess.Popen(cmd)

    def add_user(self) -> None:
        if not ctx.admin:
            return

        dialog = AddUserDialog(self)
        dialog.accepted.connect(self.login)
        dialog.open()

    def delete_user(self) -> None:
        if not ctx.admin:
            return

        dialog = DeleteUserDialog(self)
        dialog.open()

    def login(self) -> None:
        if ctx.login:
            return

        self.hide()
        dialog = LoginDialog(self)
        dialog.accepted.connect(self.logged_in)
        dialog.open()

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

    def add_contractor(self) -> None:
        if not ctx.admin:
            return

        dialog = AddContractorDialog(self)
        dialog.open()

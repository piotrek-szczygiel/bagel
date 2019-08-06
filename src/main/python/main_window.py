import os
import subprocess

from PySide2.QtWidgets import QMainWindow, QMessageBox

from add_contractor import AddContractor
from add_user import AddUser
from ctx import ctx
from delete_user import DeleteUser
from login import Login
from main_widget import MainWidget
from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, db_path) -> None:
        super(MainWindow, self).__init__()

        self.db_path = db_path

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_open_dir.triggered.connect(self.open_dir)

        self.ui.action_login.triggered.connect(self.login)
        self.ui.action_logout.triggered.connect(self.logout)
        self.ui.action_add_user.triggered.connect(self.add_user)
        self.ui.action_delete_user.triggered.connect(self.delete_user)

        self.ui.action_add_contractor.triggered.connect(self.add_contractor)
        self.refresh_actions()
        self.show()

    def refresh_actions(self) -> None:
        self.ui.action_login.setEnabled(not ctx.logged_in)
        self.ui.action_logout.setEnabled(ctx.logged_in)
        self.ui.action_add_user.setEnabled(ctx.admin)
        self.ui.action_delete_user.setEnabled(ctx.admin)
        self.ui.action_add_contractor.setEnabled(ctx.admin)
        self.ui.action_edit_contractor.setEnabled(ctx.admin)

    def open_dir(self) -> None:
        if os.name == "nt":
            cmd = f'explorer /select,"{self.db_path}"'
            subprocess.Popen(cmd)

    def add_user(self, first_time=False) -> None:
        if not ctx.admin and not first_time:
            return

        w = AddUser(self)

        if first_time:
            w.ui.combo_type.setDisabled(True)
            w.ui.combo_type.setCurrentIndex(1)
            w.ui.label_title.setText("Dodaj administratora")

        if ctx.logged_in:
            w.finished.connect(self.logged_in)
        elif not first_time:
            w.finished.connect(self.login)
        elif first_time:

            def slot(success: bool) -> None:
                if success:
                    self.login()
                else:
                    self.close()

            w.finished.connect(slot)

        w.ui.input_login.setFocus()
        self.setCentralWidget(w)

    def delete_user(self) -> None:
        if not ctx.admin:
            return

        w = DeleteUser(self)
        w.ui.combo_users.setFocus()
        self.setCentralWidget(w)

    def login(self) -> None:
        if ctx.logged_in:
            return

        w = Login(self)
        w.finished.connect(self.logged_in)
        w.ui.input_login.setFocus()
        self.setCentralWidget(w)

    def logged_in(self) -> None:
        if not ctx.logged_in:
            return

        self.setWindowTitle(
            "Bagel - " + ctx.login + " (Administrator)" if ctx.admin else ""
        )

        self.refresh_actions()
        self.setCentralWidget(MainWidget(self))

    def logout(self, ask=True) -> None:
        if not ctx.login:
            return

        if ask:
            answer = QMessageBox.question(
                self, "Potwierdzenie wylogowania", "Czy na pewno chcesz się wylogować?"
            )

            if answer == QMessageBox.No:
                return

        ctx.logged_in = False
        ctx.login = ""
        ctx.admin = False

        self.setWindowTitle("Bagel")

        self.refresh_actions()
        self.login()

    def add_contractor(self) -> None:
        if not ctx.admin:
            return

        w = AddContractor(self)
        w.ui.input_first_name.setFocus()
        self.setCentralWidget(w)

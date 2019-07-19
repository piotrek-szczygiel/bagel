import os
import sqlite3
import sys

from appdirs import user_data_dir
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow

from add_user_dialog import AddUserDialog
from ctx import ctx
from login_dialog import LoginDialog
from main_window import MainWindow


class Main:
    def __init__(self) -> None:
        self.main_window: QMainWindow
        self.db_dir = user_data_dir("Bagel", "Angoland")

    def start(self):
        ctx.app_ctx = ApplicationContext()

        db_path = os.path.join(self.db_dir, "database.db")

        if not os.path.isdir(self.db_dir):
            os.makedirs(self.db_dir)

        ctx.db = sqlite3.connect(db_path)

        c = ctx.db.cursor()

        try:
            c.execute("select * from users")
        except sqlite3.OperationalError:
            c.execute(
                r"""
                CREATE TABLE "users"
                (
                    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "login"	    TEXT NOT NULL UNIQUE,
                    "password"  TEXT NOT NULL,
                    "admin"     INTEGER NOT NULL DEFAULT 0
                )
                """
            )
            ctx.db.commit()

        add_admin = False

        if c.fetchone() is None:
            add_admin = True

        self.main_window = MainWindow()
        self.main_window.show()

        if add_admin:
            add_user_dialog = AddUserDialog(self.main_window)
            add_user_dialog.ui.combo_type.setDisabled(True)
            add_user_dialog.ui.combo_type.setCurrentIndex(1)
            add_user_dialog.ui.label_title.setText("Dodaj administratora")
            add_user_dialog.accepted.connect(self.login)
            add_user_dialog.open()
        else:
            self.login()

        exit_code = ctx.app_ctx.app.exec_()
        sys.exit(exit_code)

    def login(self) -> None:
        login_dialog = LoginDialog(self.main_window)
        login_dialog.accepted.connect(self.logged_in)
        login_dialog.open()

    def logged_in(self) -> None:
        if ctx.login:
            self.main_window.setWindowTitle("Bagel v0.1.0 - " + ctx.login)

        for i in range(1, 11):
            self.main_window.ui.list_sellers.addItem("Test " + str(i))


if __name__ == "__main__":
    Main().start()

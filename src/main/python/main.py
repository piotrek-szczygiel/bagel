import os
import sqlite3
import sys

from appdirs import user_data_dir
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow

from add_user_dialog import AddUserDialog
from ctx import ctx
from main_window import MainWindow


class Main:
    def __init__(self) -> None:
        self.main_window: QMainWindow
        self.db_path = ""

        ctx.main = self

    def start(self):
        ctx.app_ctx = ApplicationContext()

        db_dir = user_data_dir("Bagel", "Angoland")

        self.db_path = os.path.join(db_dir, "baza_danych.db")

        if not os.path.isdir(db_dir):
            os.makedirs(db_dir)

        ctx.db = sqlite3.connect(self.db_path)

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
                    "admin"     INTEGER NOT NULL
                )
                """
            )
            ctx.db.commit()

        try:
            c.execute("select * from contractors")
        except sqlite3.OperationalError:
            c.execute(
                r"""
                CREATE TABLE "contractors"
                (
                    "id"            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "first_name"    TEXT NOT NULL,
                    "last_name"     TEXT NOT NULL,
                    "zip_code"      INTEGER NOT NULL,
                    "city"          TEXT NOT NULL,
                    "street"        TEXT NOT NULL,
                    "company_name"  TEXT NOT NULL,
                    "nip"           INTEGER NOT NULL,
                    "regon"         INTEGER NOT NULL
                )
                """
            )
            ctx.db.commit()

        add_admin = True

        c.execute("select * from users")
        for user in c.fetchall():
            if user[3] == 1:
                add_admin = False
                break

        self.main_window = MainWindow(self.db_path)

        if add_admin:
            add_user_dialog = AddUserDialog(self.main_window)
            add_user_dialog.ui.combo_type.setDisabled(True)
            add_user_dialog.ui.combo_type.setCurrentIndex(1)
            add_user_dialog.ui.label_title.setText("Dodaj administratora")
            add_user_dialog.setWindowTitle("Dodaj administratora")
            add_user_dialog.accepted.connect(self.main_window.login)
            add_user_dialog.open()
        else:
            self.main_window.login()

        exit_code = ctx.app_ctx.app.exec_()
        sys.exit(exit_code)


if __name__ == "__main__":
    Main().start()

import os
import sqlite3
import sys

from appdirs import user_data_dir
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMessageBox

from ctx import ctx
from main_window import MainWindow

if __name__ == "__main__":
    ctx.app_ctx = ApplicationContext()

    db_dir = user_data_dir("Bagel", "Angoland")
    db_path = os.path.join(db_dir, "database.db")

    if not os.path.isdir(db_dir):
        os.makedirs(db_dir)

    ctx.db = sqlite3.connect(db_path)

    c = ctx.db.cursor()

    try:
        c.execute("select * from users")
    except sqlite3.OperationalError:
        c.execute(
            r"""
CREATE TABLE "users" (
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "login"	    TEXT NOT NULL UNIQUE,
    "password"  TEXT NOT NULL,
    "admin"     INTEGER NOT NULL DEFAULT 0
)
"""
        )
        ctx.db.commit()

    if c.fetchone() is None:
        answer = QMessageBox.question(
            None,
            "Brak użytkowników",
            "Nie znaleziono żadnego użytkownika.\n"
            + "Czy chcesz go teraz utworzyć?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if answer == QMessageBox.Yes:
            pass
        else:
            sys.exit(0)

    ctx.main_window = MainWindow()

    ctx.main_window.show()

    ctx.log("Otwieranie bazy danych")

    ctx.main_window.login_dialog.show()
    ctx.log("Oczekiwanie na zalogowanie...")

    exit_code = ctx.app_ctx.app.exec_()
    sys.exit(exit_code)

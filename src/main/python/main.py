import os
import sqlite3
import sys

from appdirs import user_data_dir
from fbs_runtime.application_context.PySide2 import ApplicationContext

from add_user_dialog import AddUserDialog
from ctx import ctx
from login_dialog import LoginDialog
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

    ctx.main_window = MainWindow()
    ctx.main_window.show()

    if add_admin:
        add_user_dialog = AddUserDialog(ctx.main_window)
        add_user_dialog.ui.combo_type.setDisabled(True)
        add_user_dialog.ui.combo_type.setCurrentIndex(1)
        add_user_dialog.ui.label_title.setText("Dodaj administratora")
        add_user_dialog.show()
    else:
        login_dialog = LoginDialog(ctx.main_window)
        login_dialog.show()

    exit_code = ctx.app_ctx.app.exec_()
    sys.exit(exit_code)

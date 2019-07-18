import sqlite3

from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow


class Ctx:
    def __init__(self) -> None:
        self.app_ctx: ApplicationContext
        self.db: sqlite3.Connection
        self.main_window: QMainWindow

    def resource(self, name: str) -> str:
        return self.app_ctx.get_resource(name)

    def log(self, message: str, timeout: int = 0) -> None:
        self.main_window.ui.statusBar.showMessage(message, timeout)
        print(f"log: {message}")


ctx = Ctx()

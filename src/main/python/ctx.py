import sqlite3
from typing import Any

from fbs_runtime.application_context.PySide2 import ApplicationContext


class Ctx:
    def __init__(self) -> None:
        self.app_ctx: ApplicationContext
        self.db: sqlite3.Connection
        self.main: Any

        self.login: str = ""
        self.admin = False

    def resource(self, name: str) -> str:
        return self.app_ctx.get_resource(name)


ctx = Ctx()

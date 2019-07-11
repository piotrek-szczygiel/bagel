import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow


if __name__ == "__main__":
    context = ApplicationContext()

    window = QMainWindow()
    window.resize(250, 150)
    window.show()

    exit_code = context.app.exec_()
    sys.exit(exit_code)

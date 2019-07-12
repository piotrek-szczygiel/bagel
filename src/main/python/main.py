from fbs_runtime.application_context.PySide2 import ApplicationContext
from ui.main import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QMessageBox

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_1.clicked.connect(
            lambda: QMessageBox.information(self, "Title", "Text")
        )


if __name__ == "__main__":
    ctx = ApplicationContext()
    ctx.app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    exit_code = ctx.app.exec_()
    sys.exit(exit_code)

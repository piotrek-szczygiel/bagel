from fbs_runtime.application_context.PySide2 import ApplicationContext
from ui.main_window import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow

import sys

ctx = ApplicationContext()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.close)

        self.ui.listWidget_sellers.addItem("Test 1")
        self.ui.listWidget_sellers.addItem("Test 2")


if __name__ == "__main__":
    window = MainWindow()
    window.show()

    exit_code = ctx.app.exec_()
    sys.exit(exit_code)

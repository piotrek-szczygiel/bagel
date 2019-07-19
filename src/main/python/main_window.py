from PySide2.QtWidgets import QMainWindow

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.close)

        self.ui.listWidget_sellers.addItem("Test 1")
        self.ui.listWidget_sellers.addItem("Test 2")

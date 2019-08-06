from PySide2.QtWidgets import QWidget

from ui.main_widget import Ui_MainWidget


class MainWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super(MainWidget, self).__init__(parent)
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

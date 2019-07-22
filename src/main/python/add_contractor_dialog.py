from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog

from ctx import ctx
from ui.add_contractor_dialog import Ui_AddContractorDialog


class AddContractorDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(AddContractorDialog, self).__init__(parent)
        self.ui = Ui_AddContractorDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(
            QPixmap(ctx.resource("add_contractor.png"))
        )

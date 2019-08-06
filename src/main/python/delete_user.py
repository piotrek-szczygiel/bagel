from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from ctx import ctx
from ui.delete_user import Ui_DeleteUser


class DeleteUser(QWidget):
    finished = Signal()

    def __init__(self, parent=None) -> None:
        super(DeleteUser, self).__init__(parent)
        self.ui = Ui_DeleteUser()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Widget)
        self.ui.label_logo.setPixmap(QPixmap(ctx.resource("delete_user.png")))
        self.ui.button_delete.clicked.connect(self.delete_user)

        c = ctx.db.cursor()
        c.execute("select * from users")
        for user in c.fetchall():
            self.ui.combo_users.addItem(user[1])

    def delete_user(self) -> None:
        login = self.ui.combo_users.currentText()

        answer = QMessageBox.question(
            self,
            "Potwierdź usunięcie użytkownika",
            f"Czy na pewno chcesz usunąć użytkownika {login}?",
        )

        if answer == QMessageBox.No:
            return

        c = ctx.db.cursor()
        c.execute("delete from users where login=?", (login,))

        if c.rowcount == 1:
            ctx.db.commit()

            QMessageBox.information(
                self, "Sukces", f"Pomyślnie usunięto użytkownika {login}"
            )

            if ctx.login == login:
                ctx.main.main_window.logout(False)

            self.finished.emit()
        else:
            QMessageBox.critical(
                self, "Błąd", f"Nie udało się usunąć użytkownika {login}"
            )

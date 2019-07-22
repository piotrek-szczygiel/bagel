from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QMessageBox

from ctx import ctx
from ui.delete_user_dialog import Ui_DeleteUserDialog


class DeleteUserDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(DeleteUserDialog, self).__init__(parent)
        self.ui = Ui_DeleteUserDialog()
        self.ui.setupUi(self)
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

            self.accept()
        else:
            QMessageBox.critical(
                self, "Błąd", f"Nie udało się usunąć użytkownika {login}"
            )

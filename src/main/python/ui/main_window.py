# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\build\ui\main_window.ui',
# licensing of 'src\build\ui\main_window.ui' applies.
#
# Created: Tue Aug  6 19:10:23 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Bagel v0.1.0")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Plik = QtWidgets.QMenu(self.menubar)
        self.menu_Plik.setObjectName("menu_Plik")
        self.menu_U_ytkownik = QtWidgets.QMenu(self.menubar)
        self.menu_U_ytkownik.setObjectName("menu_U_ytkownik")
        self.menu_Kontrahenci = QtWidgets.QMenu(self.menubar)
        self.menu_Kontrahenci.setObjectName("menu_Kontrahenci")
        MainWindow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_open_dir = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.action_open_dir.setFont(font)
        self.action_open_dir.setObjectName("action_open_dir")
        self.action_add_user = QtWidgets.QAction(MainWindow)
        self.action_add_user.setEnabled(False)
        self.action_add_user.setObjectName("action_add_user")
        self.action_logout = QtWidgets.QAction(MainWindow)
        self.action_logout.setEnabled(False)
        self.action_logout.setObjectName("action_logout")
        self.action_delete_user = QtWidgets.QAction(MainWindow)
        self.action_delete_user.setEnabled(False)
        self.action_delete_user.setObjectName("action_delete_user")
        self.action_add_contractor = QtWidgets.QAction(MainWindow)
        self.action_add_contractor.setEnabled(False)
        self.action_add_contractor.setObjectName("action_add_contractor")
        self.action_edit_contractor = QtWidgets.QAction(MainWindow)
        self.action_edit_contractor.setEnabled(False)
        self.action_edit_contractor.setObjectName("action_edit_contractor")
        self.action_login = QtWidgets.QAction(MainWindow)
        self.action_login.setEnabled(False)
        self.action_login.setObjectName("action_login")
        self.menu_Plik.addAction(self.action_open_dir)
        self.menu_Plik.addSeparator()
        self.menu_Plik.addAction(self.action_exit)
        self.menu_U_ytkownik.addAction(self.action_login)
        self.menu_U_ytkownik.addAction(self.action_logout)
        self.menu_U_ytkownik.addSeparator()
        self.menu_U_ytkownik.addAction(self.action_add_user)
        self.menu_U_ytkownik.addAction(self.action_delete_user)
        self.menu_Kontrahenci.addAction(self.action_add_contractor)
        self.menu_Kontrahenci.addAction(self.action_edit_contractor)
        self.menubar.addAction(self.menu_Plik.menuAction())
        self.menubar.addAction(self.menu_U_ytkownik.menuAction())
        self.menubar.addAction(self.menu_Kontrahenci.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.menu_Plik.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Plik", None, -1))
        self.menu_U_ytkownik.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Użytkownicy", None, -1))
        self.menu_Kontrahenci.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Kontrahenci", None, -1))
        self.action_exit.setText(QtWidgets.QApplication.translate("MainWindow", "&Wyjdź", None, -1))
        self.action_open_dir.setText(QtWidgets.QApplication.translate("MainWindow", "&Otwórz folder z bazą", None, -1))
        self.action_add_user.setText(QtWidgets.QApplication.translate("MainWindow", "&Dodaj użytkownika", None, -1))
        self.action_logout.setText(QtWidgets.QApplication.translate("MainWindow", "&Wyloguj", None, -1))
        self.action_delete_user.setText(QtWidgets.QApplication.translate("MainWindow", "&Usuń użytkownika", None, -1))
        self.action_add_contractor.setText(QtWidgets.QApplication.translate("MainWindow", "&Dodaj kontrahenta", None, -1))
        self.action_edit_contractor.setText(QtWidgets.QApplication.translate("MainWindow", "&Edytuj kontrahenta", None, -1))
        self.action_login.setText(QtWidgets.QApplication.translate("MainWindow", "&Zaloguj", None, -1))


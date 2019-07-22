# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\build\ui\login_dialog.ui',
# licensing of 'src\build\ui\login_dialog.ui' applies.
#
# Created: Mon Jul 22 20:10:16 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LoginDialog.resize(400, 250)
        LoginDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_logo = QtWidgets.QLabel(LoginDialog)
        self.label_logo.setMinimumSize(QtCore.QSize(80, 80))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.input_login = QtWidgets.QLineEdit(LoginDialog)
        self.input_login.setPlaceholderText("")
        self.input_login.setClearButtonEnabled(True)
        self.input_login.setObjectName("input_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_login)
        self.label_4 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.input_password = QtWidgets.QLineEdit(LoginDialog)
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setPlaceholderText("")
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_password)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.button_login = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_login.sizePolicy().hasHeightForWidth())
        self.button_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_login.setFont(font)
        self.button_login.setCheckable(False)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout_2.addWidget(self.button_login)
        self.button_cancel = QtWidgets.QPushButton(LoginDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_cancel.setFont(font)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_2.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtWidgets.QApplication.translate("LoginDialog", "Logowanie", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("LoginDialog", "Logowanie", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("LoginDialog", "Login:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("LoginDialog", "Hasło:", None, -1))
        self.button_login.setText(QtWidgets.QApplication.translate("LoginDialog", "Zaloguj", None, -1))
        self.button_cancel.setText(QtWidgets.QApplication.translate("LoginDialog", "Anuluj", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\build\ui\delete_user.ui',
# licensing of 'src\build\ui\delete_user.ui' applies.
#
# Created: Tue Aug  6 19:10:26 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DeleteUser(object):
    def setupUi(self, DeleteUser):
        DeleteUser.setObjectName("DeleteUser")
        DeleteUser.resize(516, 239)
        self.verticalLayout = QtWidgets.QVBoxLayout(DeleteUser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_logo = QtWidgets.QLabel(DeleteUser)
        self.label_logo.setMinimumSize(QtCore.QSize(80, 80))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_2.addWidget(self.label_logo)
        self.label_2 = QtWidgets.QLabel(DeleteUser)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DeleteUser)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.combo_users = QtWidgets.QComboBox(DeleteUser)
        self.combo_users.setObjectName("combo_users")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_users)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.button_delete = QtWidgets.QPushButton(DeleteUser)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_delete.setFont(font)
        self.button_delete.setDefault(True)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(DeleteUser)
        QtCore.QMetaObject.connectSlotsByName(DeleteUser)

    def retranslateUi(self, DeleteUser):
        self.label_2.setText(QtWidgets.QApplication.translate("DeleteUser", "Usuń użytkownika", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DeleteUser", "Nazwa użytkownika:", None, -1))
        self.button_delete.setText(QtWidgets.QApplication.translate("DeleteUser", "Usuń", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\bagel\src\build\ui\add_contractor_dialog.ui',
# licensing of 'C:\dev\bagel\src\build\ui\add_contractor_dialog.ui' applies.
#
# Created: Mon Jul 22 02:27:00 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AddContractorDialog(object):
    def setupUi(self, AddContractorDialog):
        AddContractorDialog.setObjectName("AddContractorDialog")
        AddContractorDialog.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddContractorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_logo = QtWidgets.QLabel(AddContractorDialog)
        self.label_logo.setMinimumSize(QtCore.QSize(90, 0))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        self.label_2 = QtWidgets.QLabel(AddContractorDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(AddContractorDialog)
        QtCore.QMetaObject.connectSlotsByName(AddContractorDialog)

    def retranslateUi(self, AddContractorDialog):
        AddContractorDialog.setWindowTitle(QtWidgets.QApplication.translate("AddContractorDialog", "Dodaj kontrahenta", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("AddContractorDialog", "Dodaj kontrahenta", None, -1))


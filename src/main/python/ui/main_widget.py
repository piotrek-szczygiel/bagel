# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\build\ui\main_widget.ui',
# licensing of 'src\build\ui\main_widget.ui' applies.
#
# Created: Tue Aug  6 19:10:24 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(800, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sales = QtWidgets.QWidget()
        self.tab_sales.setObjectName("tab_sales")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_sales)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_sellers = QtWidgets.QListWidget(self.tab_sales)
        self.list_sellers.setObjectName("list_sellers")
        self.horizontalLayout_2.addWidget(self.list_sellers)
        self.groupBox = QtWidgets.QGroupBox(self.tab_sales)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_sales, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_documents = QtWidgets.QWidget()
        self.tab_documents.setObjectName("tab_documents")
        self.tabWidget.addTab(self.tab_documents, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(MainWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWidget", "Szczegółowe informacje o sprzedawcy", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sales), QtWidgets.QApplication.translate("MainWidget", "Sprzedaż", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWidget", "Kontrahenci", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_documents), QtWidgets.QApplication.translate("MainWidget", "Dokumenty", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QtWidgets.QApplication.translate("MainWidget", "Opcje", None, -1))


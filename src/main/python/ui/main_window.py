# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\bagel\src\build\ui\main_window.ui',
# licensing of 'C:\dev\bagel\src\build\ui\main_window.ui' applies.
#
# Created: Wed Jul 17 03:12:29 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowTitle("Bagel v0.1.0")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sales = QtWidgets.QWidget()
        self.tab_sales.setObjectName("tab_sales")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_sales)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_sellers = QtWidgets.QListWidget(self.tab_sales)
        self.listWidget_sellers.setObjectName("listWidget_sellers")
        self.horizontalLayout_2.addWidget(self.listWidget_sellers)
        self.groupBox = QtWidgets.QGroupBox(self.tab_sales)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_sales, "")
        self.tab_documents = QtWidgets.QWidget()
        self.tab_documents.setObjectName("tab_documents")
        self.tabWidget.addTab(self.tab_documents, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Plik = QtWidgets.QMenu(self.menubar)
        self.menu_Plik.setObjectName("menu_Plik")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_Plik.addAction(self.actionExit)
        self.menubar.addAction(self.menu_Plik.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Szczegółowe informacje o sprzedawcy", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sales), QtWidgets.QApplication.translate("MainWindow", "Sprzedaż", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_documents), QtWidgets.QApplication.translate("MainWindow", "Dokumenty", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QtWidgets.QApplication.translate("MainWindow", "Opcje", None, -1))
        self.menu_Plik.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Plik", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Wyjdź", None, -1))


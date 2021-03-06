# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ABR.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Pause_Button = QtWidgets.QPushButton(self.frame)
        self.Pause_Button.setObjectName("Pause_Button")
        self.gridLayout_2.addWidget(self.Pause_Button, 0, 5, 1, 1)
        self.Data_File = QtWidgets.QLabel(self.frame)
        self.Data_File.setObjectName("Data_File")
        self.gridLayout_2.addWidget(self.Data_File, 0, 0, 1, 1)
        self.Stop_Button = QtWidgets.QPushButton(self.frame)
        self.Stop_Button.setObjectName("Stop_Button")
        self.gridLayout_2.addWidget(self.Stop_Button, 0, 4, 1, 1)
        self.DATA_File_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.DATA_File_lineEdit.setObjectName("DATA_File_lineEdit")
        self.gridLayout_2.addWidget(self.DATA_File_lineEdit, 0, 1, 1, 1)
        self.Start_Button = QtWidgets.QPushButton(self.frame)
        self.Start_Button.setObjectName("Start_Button")
        self.gridLayout_2.addWidget(self.Start_Button, 0, 3, 1, 1)
        self.Browse_Path_Button = QtWidgets.QToolButton(self.frame)
        self.Browse_Path_Button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Browse_Path_Button.setToolTipDuration(4)
        self.Browse_Path_Button.setAutoRaise(False)
        self.Browse_Path_Button.setObjectName("Browse_Path_Button")
        self.gridLayout_2.addWidget(self.Browse_Path_Button, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 6, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(self.frame_2)
        self.graphicsView.setMaximumSize(QtCore.QSize(900, 16777215))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_2)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionReadMe = QtWidgets.QAction(MainWindow)
        self.actionReadMe.setObjectName("actionReadMe")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionReadMe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation Tool - 0.112345"))
        self.Pause_Button.setText(_translate("MainWindow", "Pause"))
        self.Data_File.setText(_translate("MainWindow", "Data File"))
        self.Stop_Button.setText(_translate("MainWindow", "Stop"))
        self.DATA_File_lineEdit.setPlaceholderText(_translate("MainWindow", "Choose your Data File"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Browse_Path_Button.setText(_translate("MainWindow", "Browse"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionReadMe.setText(_translate("MainWindow", "ReadMe"))
        self.actionReadMe.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setToolTip(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
from pyqtgraph import PlotWidget

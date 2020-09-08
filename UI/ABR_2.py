# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ABR_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.Data_File_Label = QtWidgets.QLabel(self.frame)
        self.Data_File_Label.setObjectName("Data_File_Label")
        self.gridLayout.addWidget(self.Data_File_Label, 0, 0, 1, 1)
        self.Data_File_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.Data_File_lineEdit.setObjectName("Data_File_lineEdit")
        self.gridLayout.addWidget(self.Data_File_lineEdit, 0, 1, 1, 1)
        self.Browse_path_Button = QtWidgets.QToolButton(self.frame)
        self.Browse_path_Button.setObjectName("Browse_path_Button")
        self.gridLayout.addWidget(self.Browse_path_Button, 0, 2, 1, 1)
        self.Plot_PushButton = QtWidgets.QPushButton(self.frame)
        self.Plot_PushButton.setObjectName("Plot_PushButton")
        self.gridLayout.addWidget(self.Plot_PushButton, 0, 3, 1, 1)
        self.Clear_PushButton = QtWidgets.QPushButton(self.frame)
        self.Clear_PushButton.setObjectName("Clear_PushButton")
        self.gridLayout.addWidget(self.Clear_PushButton, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView = PlotWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.frame_2)
        self.treeView.setObjectName("treeView")
        self.gridLayout_4.addWidget(self.treeView, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Data_File_Label.setText(_translate("MainWindow", "Data File"))
        self.Browse_path_Button.setText(_translate("MainWindow", "Browse"))
        self.Plot_PushButton.setText(_translate("MainWindow", "Plot"))
        self.Clear_PushButton.setText(_translate("MainWindow", "Clear"))
from pyqtgraph import PlotWidget

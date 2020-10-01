# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ABR_3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 593)
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
        self.Left_Ear_Rec_1 = QtWidgets.QCheckBox(self.frame)
        self.Left_Ear_Rec_1.setObjectName("Left_Ear_Rec_1")
        self.gridLayout.addWidget(self.Left_Ear_Rec_1, 0, 7, 1, 1)
        self.Plot = QtWidgets.QPushButton(self.frame)
        self.Plot.setObjectName("Plot")
        self.gridLayout.addWidget(self.Plot, 0, 4, 1, 1)
        self.Data_File_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.Data_File_lineEdit.setObjectName("Data_File_lineEdit")
        self.gridLayout.addWidget(self.Data_File_lineEdit, 0, 1, 1, 1)
        self.Left_Ear_Rec_2 = QtWidgets.QCheckBox(self.frame)
        self.Left_Ear_Rec_2.setObjectName("Left_Ear_Rec_2")
        self.gridLayout.addWidget(self.Left_Ear_Rec_2, 0, 8, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 11, 1, 1)
        self.Diff_Checkbox = QtWidgets.QCheckBox(self.frame)
        self.Diff_Checkbox.setObjectName("Diff_Checkbox")
        self.gridLayout.addWidget(self.Diff_Checkbox, 0, 9, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 15, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 10, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 12, 1, 1)
        self.Right_Ear_Rec_1 = QtWidgets.QCheckBox(self.frame)
        self.Right_Ear_Rec_1.setObjectName("Right_Ear_Rec_1")
        self.gridLayout.addWidget(self.Right_Ear_Rec_1, 0, 5, 1, 1)
        self.Clear_PushButton = QtWidgets.QPushButton(self.frame)
        self.Clear_PushButton.setObjectName("Clear_PushButton")
        self.gridLayout.addWidget(self.Clear_PushButton, 0, 3, 1, 1)
        self.Browse_path_Button = QtWidgets.QToolButton(self.frame)
        self.Browse_path_Button.setObjectName("Browse_path_Button")
        self.gridLayout.addWidget(self.Browse_path_Button, 0, 2, 1, 1)
        self.Right_Ear_Rec_2 = QtWidgets.QCheckBox(self.frame)
        self.Right_Ear_Rec_2.setObjectName("Right_Ear_Rec_2")
        self.gridLayout.addWidget(self.Right_Ear_Rec_2, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(70, 80))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 13, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 14, 1, 1)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = pg.GraphicsLayoutWidget(self.frame_2)
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
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 2)
        self.First_table = QtWidgets.QTableWidget(self.frame_2)
        self.First_table.setMaximumSize(QtCore.QSize(850, 140))
        self.First_table.setGridStyle(QtCore.Qt.SolidLine)
        self.First_table.setObjectName("First_table")
        self.First_table.setColumnCount(7)
        self.First_table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.First_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.First_table, 1, 0, 1, 1)
        self.PN_table = QtWidgets.QTableWidget(self.frame_2)
        self.PN_table.setEnabled(True)
        self.PN_table.setMaximumSize(QtCore.QSize(450, 140))
        self.PN_table.setObjectName("PN_table")
        self.PN_table.setColumnCount(4)
        self.PN_table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PN_table.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.PN_table, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABR Simulation"))
        self.Data_File_Label.setText(_translate("MainWindow", "Data File"))
        self.Left_Ear_Rec_1.setText(_translate("MainWindow", "Left Ear Rec 1"))
        self.Plot.setText(_translate("MainWindow", "Plot"))
        self.Left_Ear_Rec_2.setText(_translate("MainWindow", "Left Ear Rec 2"))
        self.Diff_Checkbox.setText(_translate("MainWindow", "Difference of Graphs"))
        self.label_2.setText(_translate("MainWindow", "Range for Correlation"))
        self.Right_Ear_Rec_1.setText(_translate("MainWindow", "Right Ear Rec 1"))
        self.Clear_PushButton.setText(_translate("MainWindow", "Clear"))
        self.Browse_path_Button.setText(_translate("MainWindow", "Browse"))
        self.Right_Ear_Rec_2.setText(_translate("MainWindow", "Right Ear Rec 2"))
        self.label.setText(_translate("MainWindow", "Correlation"))
        item = self.First_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Latency (ms)"))
        item = self.First_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amplitude (uV)"))
        item = self.First_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "l"))
        item = self.First_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "l\'"))
        item = self.First_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ll"))
        item = self.First_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "lll"))
        item = self.First_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "lV"))
        item = self.First_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Vl"))
        item = self.First_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "V\'"))
        item = self.PN_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P1"))
        item = self.PN_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N1"))
        item = self.PN_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P2"))
        item = self.PN_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "N2"))
from pyqtgraph import GraphicsLayoutWidget

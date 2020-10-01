from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QProgressBar
from PyQt5.Qt import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import xlrd
import sys
import numpy as np

from UI import ABR_3  # importing our generated file


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = ABR_3.Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.Browse_path_Button.clicked.connect(self.select_DataFile)
        # self.ui.actionReadMe.triggered.connect(self.open_README)
        # self.ui.Start_Button.setEnabled(False)
        self.file_selected = False
        self.ui.Clear_PushButton.clicked.connect(self.clear_Fields)
        self.ui.Plot.clicked.connect(self.plot)
        # self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.graphicsView.setBackground('w')
        self.p1 = self.ui.graphicsView.addPlot(row=0, col=0)
        self.p1.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.p1.getAxis("bottom").setTextPen(color='k')
        self.p1.getAxis("left").setTextPen(color='k')
        styles = {'font-size': '20px'}
        self.p1.setLabel('left','Ampltitude(uV)' , **styles)
        self.p1.setLabel('bottom','Latency(msec)' , **styles)
        self.p1.showGrid(x=True, y=True)
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.p1.getAxis("bottom").setStyle(tickFont=font, tickTextOffset=20)
        self.p1.getAxis("left").setStyle(tickFont=font, tickTextOffset=20)
        self.p1.ctrl.fftCheck.toggled.connect(self.updateLabels)


        # Row increment variable in table widget
        self.i = 0
        # pg.dbg()
        self.p1.setAutoVisible(y=True)
        self.vb = self.p1.vb


    def select_DataFile(self):
        self.x_axis = []
        self.y1_axis = []
        self.y2_axis = []
        self.y3_axis = []
        self.y4_axis = []
        self.correlation_range = []
        self.correlation_array_y1 = []
        self.correlation_array_y2 = []
        self.correlation_array_y3 = []
        self.correlation_array_y4 = []
        self.y1_y2_diff = []
        self.y3_y4_diff = []

        # self.vb = self.p1.vb

        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Data File')
        if not file_path:
            QtWidgets.QMessageBox.about(self, 'Path required', '1. Please select a Data file!\n or\n 2. If selected click Start!')
            return
        # log_file = open(file_path, 'r')

        if file_path:
            self.ui.Data_File_lineEdit.setText(file_path)
            self.file = file_path
            # self.ui.DATA_ARRAY_FROM_CANLOG = open(file_path).read().splitlines()      # Read the file as an array
            # To open Workbook
            wb = xlrd.open_workbook(file_path)
            sheet = wb.sheet_by_index(0)
            for i in range(sheet.nrows):
                self.x_axis.append(sheet.cell_value(i, 0))
                self.y1_axis.append(sheet.cell_value(i, 1))
                self.y2_axis.append(sheet.cell_value(i, 2))
                self.y3_axis.append(sheet.cell_value(i, 3))
                self.y4_axis.append(sheet.cell_value(i, 4))

            self.x_axis.pop(0)
            self.y1_axis.pop(0)
            self.y2_axis.pop(0)
            self.y3_axis.pop(0)
            self.y4_axis.pop(0)
            self.p1.setXRange(self.x_axis[1], self.x_axis[-1], padding=0)

    def updateLabels(self):
        styles = {'font-size': '20px'}
        self.p1.setLabel('left','Ampltitude(uV)' , **styles)
        self.p1.setLabel('bottom','Frequency' , **styles)

    def plot(self):
        pen_red = pg.mkPen(color='r', width=2)
        pen_blue = pg.mkPen(color='b', width=2)
        pen_grey = pg.mkPen(width=2)
        if self.ui.Right_Ear_Rec_1.isChecked():
            self.p1.plot(self.x_axis, self.y1_axis, pen=pen_red)
        if self.ui.Right_Ear_Rec_2.isChecked():
            self.p1.plot(self.x_axis, self.y2_axis, pen=pen_red)
        if self.ui.Left_Ear_Rec_1.isChecked():
            self.p1.plot(self.x_axis, self.y3_axis, pen=pen_blue)
        if self.ui.Left_Ear_Rec_2.isChecked():
            self.p1.plot(self.x_axis, self.y4_axis, pen=pen_blue)

        for x in range(len(self.x_axis)):
            if not self.ui.lineEdit_2.text() == ''.strip() and not self.ui.lineEdit_3.text() == ''.strip():
                if self.x_axis[x] >= int(self.ui.lineEdit_2.text()) and self.x_axis[x] <= int(self.ui.lineEdit_3.text()):
                    # print(x, self.x_axis[x])
                    self.correlation_range.append(x)
        for x in range(len(self.correlation_range)):
            self.correlation_array_y1.append(self.y1_axis[x])
            self.correlation_array_y2.append(self.y2_axis[x])
            self.correlation_array_y3.append(self.y3_axis[x])
            self.correlation_array_y4.append(self.y4_axis[x])
        if not self.ui.lineEdit_2.text() == ''.strip() and not self.ui.lineEdit_3.text() == ''.strip():
            correlation_1 = (np.corrcoef(self.correlation_array_y1, self.correlation_array_y2))
            correlation_2 = (np.corrcoef(self.correlation_array_y3, self.correlation_array_y4))
            # print(correlation_1[1][0])
            if self.ui.Right_Ear_Rec_1.isChecked() and self.ui.Right_Ear_Rec_2.isChecked():
                self.ui.lineEdit.setText(str(format(correlation_1[1][0], '.2f')))
            elif self.ui.Left_Ear_Rec_1.isChecked() and self.ui.Left_Ear_Rec_2.isChecked():
                self.ui.lineEdit.setText(str(format(correlation_2[1][0], '.2f')))

        if self.ui.Diff_Checkbox.isChecked() and self.ui.Right_Ear_Rec_1.isChecked() and self.ui.Right_Ear_Rec_2.isChecked():
            self.y1_y2_diff = np.subtract(self.y1_axis, self.y2_axis)
            self.p1.plot(self.x_axis, self.y1_y2_diff, pen=pen_grey)

        if self.ui.Diff_Checkbox.isChecked() and self.ui.Left_Ear_Rec_1.isChecked() and self.ui.Left_Ear_Rec_2.isChecked():
            self.y3_y4_diff = np.subtract(self.y3_axis, self.y4_axis)
            self.p1.plot(self.x_axis, self.y3_y4_diff, pen=pen_grey)

    def mouse_clicked(self, mouseClickEvent):
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.p1.addItem(self.vLine, ignoreBounds=True)
        self.mousePoint = self.vb.mapSceneToView(mouseClickEvent._scenePos)
        # print(self.mousePoint.x(), self.mousePoint.y(), self.mousePoint)
        x_coordinate = QTableWidgetItem(str(format(self.mousePoint.x(), '.2f')))
        y_coordinate = QTableWidgetItem(str(format(self.mousePoint.y(), '.2f')))
        if self.i <= 6 and self.x_axis[-1] <= 25:
            self.ui.First_table.setItem(0, self.i, x_coordinate)
            self.ui.First_table.setItem(1, self.i, y_coordinate)
            self.vLine.setPos(self.mousePoint.x())
            self.i += 1
        elif self.i <= 3 and self.x_axis[-1] > 25:
            self.ui.PN_table.setItem(0, self.i, x_coordinate)
            self.ui.PN_table.setItem(1, self.i, y_coordinate)
            self.vLine.setPos(self.mousePoint.x())
            self.i += 1

    def open_README(self):
        file = open("README.md", "r")
        data = file.read()
        QtWidgets.QMessageBox.about(self, 'README',data)
        return

    def clear_Fields(self):
        # self.ui.Data_File_lineEdit.clear()
        self.ui.First_table.clearContents()
        self.ui.PN_table.clearContents()
        self.p1.clear()
        self.i = 0
        self.ui.lineEdit.clear()
        self.correlation_range = []
        self.correlation_array_y1 = []
        self.correlation_array_y2 = []
        self.correlation_array_y3 = []
        self.correlation_array_y4 = []
        # self.x_axis = []
        # self.y1_axis = []
        # self.y2_axis = []
        # self.y3_axis = []
        # self.y4_axis = []

    def closeEvent(self, event):

        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Close, Cancel buttons
        """
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            self.ui.EXIT_SIMULATION_FLAG = True
            event.accept()

        else:
            event.ignore()


# class popupwindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super(popupwindow, self).__init__()
#
#         self.ui = pop_up.Ui_dialog()
#         self.setWindowIcon(QtGui.QIcon('logo.png'))



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = mywindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QProgressBar
from PyQt5.Qt import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import xlrd
import sys

from UI import ABR_2  # importing our generated file


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = ABR_2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.Browse_path_Button.clicked.connect(self.select_DataFile)
        # self.ui.actionReadMe.triggered.connect(self.open_README)
        # self.ui.Start_Button.setEnabled(False)
        self.file_selected = False
        # self.ui.Clear_PushButton.clicked.connect(self.clear_Fields)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.graphicsView.setBackground('w')
        styles = {'color': 'r', 'font-size': '20px'}
        self.ui.graphicsView.setLabel('left','Ampltitude(uV)' , **styles)
        self.ui.graphicsView.setLabel('bottom','Latency(msec)' , **styles)
        self.label = self.ui.graphicsView.setLabel('right', **styles)
        self.ui.graphicsView.showGrid(x=True, y=True)
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.ui.graphicsView.getAxis("bottom").setStyle(tickFont=font, tickTextOffset=20)
        self.ui.graphicsView.getAxis("left").setStyle(tickFont=font, tickTextOffset=20)

        self.ui.graphicsView.scene().sigMouseClicked.connect(self.mouse_clicked)

    def select_DataFile(self):
        self.x_axis = []
        self.y1_axis = []
        self.y2_axis = []
        self.y3_axis = []
        self.y4_axis = []

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

            for i in range(sheet.nrows):
                self.y1_axis.append(sheet.cell_value(i, 1))

            for i in range(sheet.nrows):
                self.y3_axis.append(sheet.cell_value(i, 2))

            for i in range(sheet.nrows):
                self.y4_axis.append(sheet.cell_value(i, 3))

            for i in range(sheet.nrows):
                self.y2_axis.append(sheet.cell_value(i, 4))
            self.x_axis.pop(0)
            self.y1_axis.pop(0)
            self.y2_axis.pop(0)
            self.y3_axis.pop(0)
            self.y4_axis.pop(0)
            self.ui.graphicsView.setXRange(self.x_axis[1], self.x_axis[-1], padding=0)

            # # plot data: x, y values
            self.plot(self.x_axis, self.y1_axis, "RightEarRecording 1 ", 'r')
            self.plot(self.x_axis, self.y2_axis, "RightEarRecording 1 ", 'r')
            self.plot(self.x_axis, self.y3_axis, "LeftEarRecording 1 ", 'b')
            self.plot(self.x_axis, self.y4_axis, "LeftEarRecording 1 ", 'b')

    def mouse_clicked(self, mouseClickEvent):
        # mouseClickEvent is a pyqtgraph.GraphicsScene.mouseEvents.MouseClickEvent
        print('clicked plot 0x{:x}, event: {}'.format(id(self), mouseClickEvent))

    def mouseMoved(self, evt):
        self.mousePoint = self.ui.graphicsView.vb.mapSceneToView(evt[0])
        self.label.setText(
            "<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>" % (
            self.mousePoint.x(), self.mousePoint.y()))

        # vb = self.ui.graphicsView.vb
        # pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        # if self.ui.graphicsView.sceneBoundingRect().contains(pos):
        #     mousePoint = vb.mapSceneToView(pos)
        #     index = int(mousePoint.x())
        #     if index > 0 and index < len(self.y1_axis):
        #         self.label.setText(
        #             "<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (
        #                 mousePoint.x(), self.y1_axis[index], self.y2_axis[index]))
        #     self.vLine.setPos(mousePoint.x())
        #     self.hLine.setPos(mousePoint.y())


    def open_README(self):
        file = open("README.md", "r")
        data = file.read()
        QtWidgets.QMessageBox.about(self, 'README',data)
        return

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color, width=2)
        self.ui.graphicsView.plot(x, y, name=plotname, pen=pen)
        # self.proxy = pg.SignalProxy(self.ui.graphicsView.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)






        # def clear_Fields(self):
    #     self.ui.Continue_Button.setEnabled(False)
    #     self.ui.CAN_File_lineEdit.clear()
    #     self.ui.tableWidget.clearContents()
    #     self.ui.treeWidget_2.clear()
    #     self.ui.DATA_ARRAY_FROM_CANLOG = None
    #     self.ui.Start_Button.setEnabled(False)
    #     self.ui.CLEAR_SIMULATION_FLAG = True              # This flag is used to stop sending WS maintenance on bus

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

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

import controller.transactionlayer
from res import getRandomPic as randompic
from view import ui


class FirstApp(ui.Ui_MainWindow):
    def __init__(self, window):
        self.datatype = ""
        self.setupUi(window)
        self.up_json.clicked.connect(self.upload_json)
        self.up_csv.clicked.connect(self.upload_csv)
        self.up_xlsx.clicked.connect(self.upload_xlsx)
        self.exp_csv.clicked.connect(self.export_CSV)
        self.exp_df.clicked.connect(self.export_DF)
        self.exp_json.clicked.connect(self.export_json)
        self.import_data.clicked.connect(self.input_handler)
        self.htmlbutton.clicked.connect(self.update_dfPrintText)
        self.rawstring.clicked.connect(self.update_dfPrintText)
        self.tl = controller.transactionlayer.TransactionLayer(self)

    def upload_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            self.datatype = "json"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.update_src_text(colnames)

    def upload_csv(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.csv)", options=options)
        if fileName:
            self.datatype = "csv"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.update_src_text(colnames)

    def upload_xlsx(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.xlsx)", options=options)
        if fileName:
            self.datatype = "xlsx"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.update_src_text(colnames)

    def upload_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            self.datatype = "json"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.update_src_text(colnames)

    def export_CSV(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", "",
                                                  "(*.csv)", options=options)
        if fileName:
            self.tl.save_file_to_csv(fileName)

    def export_DF(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", "",
                                                  "(*.pkl)", options=options)
        if fileName:
            self.tl.save_file_to_df(fileName)

    def export_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            self.tl.save_file_to_json(fileName)

    def input_handler(self):
        data = self.col_data.text()
        self.tl.get_commands_from_input(data)
        self.successLabel.setText("<b><i><u>" + self.col_data.text() + "</i></b></u>" + "                    executed!")

    def display_success_icon(self):
        path = randompic.getRandomPath()
        pixmap = QtGui.QPixmap(path)
        self.successIcon.setPixmap(pixmap)

    def update_src_text(self, colnames):
        self.textBrowser.clear()
        for col in colnames:
            self.textBrowser.append(col)

    def update_target_text(self, colnames):
        self.textBrowser_2.clear()
        for col in colnames:
            self.textBrowser_2.append(col)
        self.update_dfPrintText()
        self.display_success_icon()

    def update_dfPrintText(self):
        if self.htmlbutton.isChecked():
            data = self.tl.get_target_df().to_html()
        else:
            data = self.tl.get_target_df().to_string()
        self.dfPrint.setText(data)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)

MainWindow.show()
app.exec_()

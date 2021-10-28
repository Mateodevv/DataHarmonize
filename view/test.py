import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import controller.transactionlayer
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
        self.tl = controller.transactionlayer.TransactionLayer()

    def upload_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            self.datatype = "json"
            self.tl.file_transaction_handler(fileName, self.datatype)

    def upload_csv(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.csv)", options=options)
        if fileName:
            self.datatype = "csv"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.set_cols_in_textfield(colnames)

    def set_cols_in_textfield(self, colnames):
        self.textBrowser.clear()
        for col in colnames:
            self.textBrowser.append(col)

    def upload_xlsx(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.xlsx)", options=options)
        if fileName:
            self.datatype = "xlsx"
            colnames = self.tl.file_transaction_handler(fileName, self.datatype)
            self.set_cols_in_textfield(colnames)

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


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)

MainWindow.show()
app.exec_()

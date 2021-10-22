import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from controller import transaction_layer as tl

from view import ui


class FirstApp(ui.Ui_MainWindow):
    def __init__(self, window):
        self.datatype = ""
        self.setupUi(window)
        self.up_json.clicked.connect(self.upload_json)
        self.up_csv.clicked.connect(self.upload_csv)
        self.up_xlsx.clicked.connect(self.upload_xlsx)
        self.import_data.clicked.connect(self.input_handler)

    def upload_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            self.datatype = "json"
            tl.file_transaction_handler(fileName, self.datatype)

    def upload_csv(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.csv)", options=options)
        if fileName:
            self.datatype = "csv"
            colnames = tl.file_transaction_handler(fileName, self.datatype)
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
            colnames = tl.file_transaction_handler(fileName, self.datatype)
            self.set_cols_in_textfield(colnames)

    def input_handler(self):
        data = self.col_data.text()
        tl.data_import_handler(data, self.datatype)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)

MainWindow.show()
app.exec_()

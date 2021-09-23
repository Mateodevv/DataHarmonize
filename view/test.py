import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from controller import transaction_layer as tl

import ui


class FirstApp(ui.Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.up_json.clicked.connect(self.upload_json)
        self.up_csv.clicked.connect(self.upload_csv)
        self.up_xlsx.clicked.connect(self.upload_xlsx)
        self.import_data.clicked.connect(self.import_data_to_df)

    def upload_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.json)", options=options)
        if fileName:
            tl.file_transaction_handler(fileName, "json")

    def upload_csv(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.csv)", options=options)
        if fileName:
            colnames = tl.file_transaction_handler(fileName, "csv")
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
            colnames = tl.file_transaction_handler(fileName, "xlsx")
            self.set_cols_in_textfield(colnames)

    def import_data_to_df(self):
        text = self.col_data.text()
        self.col_data.clear() 
        print(text)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)

MainWindow.show()
app.exec_()

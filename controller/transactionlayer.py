import pandas as pd

from model.DataExtractionLayer import CSVExtractor, XLSXExtractor
from model.InterpreterEngineLayer.InteractionInterpreter import Interperter


class TransactionLayer:
    def __init__(self, app):
        self.src_df = pd.DataFrame()
        self.app = app
        self.interpreter = Interperter(self)

    def file_transaction_handler(self, fileName, dataType):
        if dataType == "csv":
            self.src_df = CSVExtractor.get_df(fileName)
            return CSVExtractor.get_csv_colnames(fileName)
        elif dataType == "json":
            pass
        elif dataType == "xlsx":
            self.src_df = XLSXExtractor.get_df(fileName)
            return XLSXExtractor.get_xlsx_colnames(fileName)

    def get_commands_from_input(self, commands):
        commands = commands.split(",")
        for command in commands:
            self.interpreter.extract_command(command, self.src_df)

    def save_file_to_csv(self, fileName):
        self.interpreter.export_csv(fileName)

    def save_file_to_df(self, fileName):
        self.interpreter.export_df(fileName)

    def save_file_to_json(self, filename):
        self.interpreter.export_json(filename)

    def update_target_ui(self, colnames):
        self.app.update_target_text(colnames)

import pandas as pd

from model.DataExtractionLayer import CSVExtractor, XLSXExtractor
import model.InterpreterEngineLayer.InteractionInterpreter as CI


class TransactionLayer:
    def __init__(self):
        self.src_df = pd.DataFrame()

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
            CI.extract_command(command, self.src_df)

    def save_file_to_csv(self, fileName):
        CI.export_csv(fileName)

    def save_file_to_df(self, fileName):
        CI.export_df(fileName)

    def save_file_to_json(self, filename):
        CI.export_json(filename)

import pandas as pd

from model.DataExtractionLayer import CSVExtractor, XLSXExtractor
from model.InterpreterEngineLayer.CommandInterpreter import extract_command


class TransactionLayer:
    def __init__(self):
        self.src_df = pd.DataFrame()

    def file_transaction_handler(self, fileName, dataType):
        if dataType == "csv":

            return CSVExtractor.get_csv_colnames(fileName)
        elif dataType == "json":
            pass
        elif dataType == "xlsx":
            self.src_df = XLSXExtractor.get_df(fileName)
            return XLSXExtractor.get_xlsx_colnames(fileName)

    def get_commands_from_input(self, commands):
        commands = commands.split(",")
        for command in commands:
            extract_command(command, self.src_df)

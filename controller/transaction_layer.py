from model.DataExtractionLayer import CSVExtractor, XLSXExtractor
from model.InterpreterEngineLayer.CommandInterpreter import extract_command
df = None


def file_transaction_handler(fileName, dataType):
    if dataType == "csv":

        return CSVExtractor.get_csv_colnames(fileName)
    elif dataType == "json":
        pass
    elif dataType == "xlsx":
        df = XLSXExtractor.get_df(fileName)
        return XLSXExtractor.get_xlsx_colnames(fileName)


def data_import_handler(data, dataType):
    if dataType == "csv":
        pass
    if dataType == "json":
        print(data, dataType, " *   * ** * * ** * ")
    if dataType == "xlsx":
        print(data, dataType, "* '* '*'*' *'*' *''''##")


def get_commands_from_input(commands):
    commands = commands.split(",")
    for command in commands:
        extract_command(command)

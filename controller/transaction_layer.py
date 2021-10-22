from model.DataExtractionLayer import CSVExtractor, XLSXExtractor
from model.InterpreterEngineLayer.CommandInterpreter import extract_command


def file_transaction_handler(fileName, dataType):
    if dataType == "csv":
        return CSVExtractor.get_csv_colnames(fileName)
    elif dataType == "json":
        None
    elif dataType == "xlsx":
        cols = XLSXExtractor.get_xlsx_colnames(fileName)
        return cols


def data_import_handler(data, dataType):
    if dataType == "csv":

    if dataType == "json":
        print(data, dataType, " *   * ** * * ** * ")
    if dataType == "xlsx":
        print(data, dataType, "* '* '*'*' *'*' *''''##")


def get_commands_from_input(commands):
    commands = commands.split(",")
    for command in commands:
        extract_command(command)

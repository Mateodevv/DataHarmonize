from model import CSVExtractor
from model import XLSXExtractor


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
        print(data, dataType, "   *********   ")
    if dataType == "json":
        print(data, dataType, " *   * ** * * ** * ")
    if dataType == "xlsx":
        print(data, dataType, "* '* '*'*' *'*' *''''##")

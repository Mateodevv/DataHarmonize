from model import CSVExtractor


def file_transaction_handler(fileName, dataType):
    if dataType == "csv":
        colnames = CSVExtractor.get_csv_colnames(fileName)
        return colnames
    elif dataType == "json":
        None
    elif dataType == "xlsx":
        None


def data_import_handler(fileName, dataType):
    if dataType == "csv":
        None
    if dataType == "json":
        None
    if dataType == "xlsx":
        None

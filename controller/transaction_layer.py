from model import CSVExtractor


def file_transaction_handler(fileName, dataType):
    if dataType == "csv":
        colnames = CSVExtractor.get_csv_colnames(fileName)
        return colnames
    elif dataType == "json":
        None
    elif dataType == "xlsx":
        None

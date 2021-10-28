import re
from model.DataFrameOperationLayer.DataFrame_Operations import DataFrameOperations

operationLayer = DataFrameOperations()


def extract_command(command, src_df):
    synval = command[command.find("(") + 1:command.find(")")]
    brackets_o = "("
    brackets_c = ")"
    src_col = command[:command.find("(")]
    target_col = command[command.find(")"):]
    if synval == "+":
        # Alle Daten von src_col werden an target_col gehängt
        operationLayer.add_column(src_df.iloc[:, int(src_col)])
    if synval == "x":
        # Daten werden auf Duplikate verglichen und unique src_col-Daten werden an target_col gehängt
        # operationLayer.append_values(src_df.iloc[:, int(src_col)])
        pass
    if synval == "-":
        # Daten aus src_col die auch in target_col vorhanden sind werden aus target_col entfernt
        print(synval + " detected")
        pass


def export_csv(filename):
    operationLayer.export_to_csv(filename)


def export_df(filename):
    operationLayer.export_df(filename)


def export_json(filename):
    operationLayer.export_json(filename)

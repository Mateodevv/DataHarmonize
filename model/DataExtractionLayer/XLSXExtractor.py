import pandas as pd
import model.utils.pandashelper as pdh


def read_excel(path, sheet=None):
    df = pd.read_excel(path, sheet_name=sheet)
    if sheet is not None:
        return df
    keys = []
    for key in df:
        keys.append(key)
    df = df[keys[0]]
    return df


def get_xlsx_colnames(fileName):
    return pdh.get_colnames(read_excel(fileName))


def get_df(path):
    return read_excel(path)

import pandas as pd


def read_excel(path, sheet=None):
    df = pd.read_excel("example_10.xlsx", sheet_name=sheet)
    if sheet is not None:
        return df
    keys = []
    for key in df:
        keys.append(key)
    df = df[keys[0]]
    return df



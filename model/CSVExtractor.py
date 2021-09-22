import pandas as pd
import model.utils.pandashelper as pdhelper


def read_csv(path):
    df = pd.read_csv(path)
    return df


def get_csv_colnames(path):
    colnames = pdhelper.get_colnames(read_csv(path))
    return colnames

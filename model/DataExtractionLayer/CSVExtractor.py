import pandas as pd
import model.utils.pandashelper as pdhelper


def read_csv(path):
    df = pd.read_csv(path)
    return df


def get_csv_colnames(path):
    return pdhelper.get_colnames(read_csv(path))


def get_df(path):
    return read_csv(path)

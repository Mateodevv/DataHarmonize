import pandas as pd

import model.utils.pandashelper as pdhelper


def read_json(path):
    df = pd.read_json(path)
    return df


def get_csv_colnames(path):
    return pdhelper.get_colnames(read_json(path))


def get_df(path):
    return read_json(path)

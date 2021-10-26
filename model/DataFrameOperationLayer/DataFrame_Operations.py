import pandas as pd


class DataFrameOperations:
    def __init__(self):
        self.target_df = pd.DataFrame()

    def add_column(self, src_col):
        self.target_df[src_col.name] = src_col.values
        print(self.target_df)

    def get_target_df(self):
        return self.target_df

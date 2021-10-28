import pandas as pd

from model.utils import pandashelper as pdh


# TODO: implement observer Pattern

class DataFrameOperations:
    def __init__(self, interpreter):
        self.target_df = pd.DataFrame()
        self.interpreter = interpreter

    def add_column(self, src_col):
        self.target_df[src_col.name] = src_col.values
        self.interpreter.update_target_ui_datapipe(pdh.get_colnames(self.target_df))

    def append_values(self, src_col, target_col):
        target_col = list(self.target_df)[int(target_col)]
        tempdf = pd.DataFrame({target_col: src_col.values})
        frames = [self.target_df, tempdf]
        self.target_df = pd.concat(frames)
        self.target_df.reset_index(drop=True, inplace=True)
        self.interpreter.update_target_ui_datapipe(pdh.get_colnames(self.target_df))

    def dropOperation(self, src_col, mode, target_col):
        target_col = list(self.target_df)[int(target_col)]
        if mode == "r":
            print(self.target_df)
            for value in src_col.tolist():
                self.target_df = self.target_df[self.target_df[target_col] == value]
            print(self.target_df)
        # drops only the value
        elif mode == "v":
            pass

        self.interpreter.update_target_ui_datapipe(pdh.get_colnames(self.target_df))

    def export_json(self, filename):
        self.target_df.to_json(filename)

    def get_target_df(self):
        return self.target_df

    def export_to_csv(self, filename):
        self.target_df.to_csv(filename, index=False)

    def export_df(self, filename):
        self.target_df.to_pickle(filename)

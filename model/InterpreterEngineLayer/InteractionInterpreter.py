from model.DataFrameOperationLayer.DataFrame_Operations import DataFrameOperations


class Interperter:
    def __init__(self, tl):
        self.tl = tl
        self.operationLayer = DataFrameOperations(self)

    def extract_command(self, command, src_df):
        synval = command[command.find("(") + 1:command.find(")")]
        brackets_o = "("
        brackets_c = ")"
        src_col = command[:command.find("(")]
        target_col = command[command.find(")") + 1:]
        if synval == "+":
            # Alle Daten von src_col werden an target_col gehängt
            self.operationLayer.add_column(src_df.iloc[:, int(src_col)])
        elif synval == "x":
            # Daten werden auf Duplikate verglichen und unique src_col-Daten werden an target_col gehängt
            self.operationLayer.append_values(src_df.iloc[:, int(src_col)], target_col)

        elif synval == "-r":
            # Daten aus src_col die auch in target_col vorhanden sind werden aus target_col entfernt
            self.operationLayer.dropOperation(src_df.iloc[:, int(src_col)], "r", target_col)
        elif synval == "-v":
            # Daten aus src_col die auch in target_col vorhanden sind werden aus target_col entfernt
            self.operationLayer.dropOperation(src_df.iloc[:, int(src_col)], "v", target_col)

    def update_target_ui_datapipe(self, colnames):
        self.tl.update_target_ui(colnames)

    def export_csv(self, filename):
        self.operationLayer.export_to_csv(filename)

    def export_df(self, filename):
        self.operationLayer.export_df(filename)

    def export_json(self, filename):
        self.operationLayer.export_json(filename)

    def get_target_df(self):
        return self.operationLayer.get_target_df()

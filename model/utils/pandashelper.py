def read_metadata(df):
    cols = []
    colsnum = df.shape[1]
    rows = df.shape[0]
    for col in df.columns:
        cols.append(col)

    return cols, colsnum, rows


def get_colnames(df):
    tmp = df.columns
    colnames = []
    i = 0
    for col in tmp:
        colnames.append(str(i) + " " + str(col))
        i += 1
    return colnames


def return_selected_columns_df(df, selected_cols=None):
    if selected_cols is not None:
        return df[selected_cols]
    else:
        return df

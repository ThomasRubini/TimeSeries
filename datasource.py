import pandas
import os

def load_example_model():
    COLUMNS = ["Dp", "R"]
    
    import statsmodels.datasets.interest_inflation.data as d
    df = d.load_pandas().data
    dates = df[["year", "quarter"]].astype(int).astype(str)
    quarterly = dates["year"] + "Q" + dates["quarter"]
    from statsmodels.tsa.base.datetools import dates_from_str
    quarterly = dates_from_str(quarterly)

    full_data = df[COLUMNS]
    full_data.index = pandas.DatetimeIndex(quarterly)

    return COLUMNS, full_data


def load_actual_model(file):

    COLUMNS = ["enrl_tot","teachers","calw_pct","meal_pct","computer","testscr","comp_stu","expn_stu","str","avginc","el_pct","read_scr","math_scr"]
    
    df = pandas.read_csv(os.path.dirname(__file__)+"/"+file)

    full_data = df[COLUMNS]


    return COLUMNS, full_data


def get_data(*, model="actual", col_n=0):
    if model == "actual":
        COLUMNS, full_data = load_actual_model("model.csv")
    elif model == "example":
        COLUMNS, full_data = load_example_model()
    else:
        raise Exception("Invalid model requested :", model)
    
    if col_n != 0:
        full_data = full_data.iloc[:, :col_n]
        COLUMNS = COLUMNS[:col_n]

    real_columns = full_data.columns
    full_data.columns = [chr(65+i) for i in range(len(full_data.columns))]
    
    return full_data, real_columns

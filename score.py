import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.vector_ar.vecm import *
import pandas
import math
from sklearn.metrics import mean_squared_error

import datasource
import prediction

full_data, REAL_COLUMNS = datasource.get_data(col_n=5)
COLUMNS = full_data.columns

def get_score(group):

    if type(group) == str:
        group = list(group)

    preds = prediction.get_predictions(full_data[group])

    return mean_squared_error(preds, full_data[group[0]].iloc[-40:], squared=False)

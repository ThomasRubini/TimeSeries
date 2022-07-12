import numpy as np
from matplotlib import pyplot as plt
import pandas

import datasource
import prediction

full_data, REAL_COLUMNS = datasource.get_data(model="actual", col_n=5)
COLUMNS = full_data.columns
pred_column = COLUMNS[0]

training = full_data.iloc[:-40]
actual_data = full_data.iloc[-40:]

pred_data = pandas.DataFrame(prediction.get_predictions(full_data))
pred_data.index = actual_data.index



# Matplotlib

# Actual data

plt.title(REAL_COLUMNS[0]+" en fonction de "+str(list(REAL_COLUMNS)))
plt.plot(training.index, training[pred_column])
plt.plot(actual_data.index, actual_data[pred_column])
plt.plot(pred_data.index, pred_data)
plt.legend(("Training", "Actual data", "Predicted data"))


plt.show()
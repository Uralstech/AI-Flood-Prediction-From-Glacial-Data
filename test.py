import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

data = pd.read_csv("test.csv")
data = data[['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'pr']]
predict = 'pr'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.5)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
#acc = linear.predict(x_test)
#print(acc)

#predictions = linear.predict(x_test)
#with open("regression_out.csv", 'w') as f:
#    f.write("Prediction,Actual\n")
#    for x in range(len(predictions)):
#        predictions[x] = predictions[x] if predictions[x] <= 20 else 20
#        predictions[x] = predictions[x] if predictions[x] >= 0 else 0
#        f.write(f'{round(predictions[x])},{y_test[x]}\n')
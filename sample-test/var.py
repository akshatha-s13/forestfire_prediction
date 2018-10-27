# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:05:50 2018

@author: AKSHATHA
"""

## This code implements Vector Auto Regression Time Series model and finds the Root Mean Square error for the features.

import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv("FFSAMPLESVM.csv")
print(df.dtypes)

df['DATE'] = pd.to_datetime(df.DATE , format = '%d-%m-%Y')
data = df.drop(['DATE'], axis=1)
data.index = df.DATE

#missing value treatment
cols = data.columns
for j in cols:
    for i in range(0,len(data)):
       if data[j][i] == ' ':
           data[j][i] = data[j][i-1]

#creating the train and validation set
train = data[:int(0.8*(len(data)))]
valid = data[int(0.8*(len(data))):]

# VAR example
from statsmodels.tsa.vector_ar.var_model import VAR

# contrived dataset with dependency
# fit model
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print(yhat)

# make prediction on validation
prediction = model_fit.forecast(model_fit.y, steps=len(valid))

#converting predictions to dataframe
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for j in range(0,4):
    for i in range(0, len(prediction)):
       pred.iloc[i][j] = prediction[i][j]

#check rmse
for i in cols:
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))


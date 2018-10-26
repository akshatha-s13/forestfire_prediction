import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
from pyramid.arima import auto_arima
y=[]
df = pd.read_csv("dehradun.csv")
print(df.dtypes)
df['DATE'] = pd.to_datetime(df.DATE , format = '%d-%m-%Y')
df["SLP"] = df.SLP.convert_objects(convert_numeric=True)
df["Precipitation"] = df.Precipitation.convert_objects(convert_numeric=True)

data=df[["TempAvg"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'30-06-2016']
valid = data.loc['01-04-2016':'30-04-2016']
stepwise_model = auto_arima(train, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=len(valid))
print(future_forecast)
prediction=future_forecast
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))


data=df[["SLP"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'30-06-2016']
valid = data.loc['01-04-2016':'30-04-2016']
stepwise_model = auto_arima(train, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=len(valid))
print(future_forecast)
prediction=future_forecast
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

data=df[["Humidity"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'30-06-2016']
valid = data.loc['01-04-2016':'30-04-2016']
stepwise_model = auto_arima(train, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=len(valid))
print(future_forecast)
prediction=future_forecast
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

data=df[["Precipitation"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'30-06-2016']
valid = data.loc['01-04-2016':'30-04-2016']
stepwise_model = auto_arima(train, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=len(valid))
print(future_forecast)
prediction=future_forecast
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

data=df[["WindSpeedMax"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'30-06-2016']
valid = data.loc['01-04-2016':'30-04-2016']
stepwise_model = auto_arima(train, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=len(valid))
print(future_forecast)
prediction=future_forecast
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))


###############################################################################################################################
## Threshold Values have to be tested to decide probability of forestfire based on predicted climate conditions for next 30 days
###############################################################################################################################
threshold=[ 10,10,10,10,10]
count_param=0
for i in (0,5):
       if y[i]>threshold[i]:
              count+=1
print("Risk of Forest Fire in next 30 days :")
if count>3:
   print ("Yes")
   




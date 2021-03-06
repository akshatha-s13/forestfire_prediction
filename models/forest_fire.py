import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
from pyramid.arima import auto_arima
y=[]
df = pd.read_csv("dehradun.csv")
print(df.dtypes)
df['DATE'] = pd.to_datetime(df.DATE , format = '%d-%m-%Y')
#df["Precipitation"] = df.Precipitation.convert_objects(convert_numeric=True)

data=df[["TempAvg"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'03-31-2016']
valid = data.loc['04-01-2016':'04-30-2016']
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
train = data.loc['01-01-2015':'03-31-2016']
valid = data.loc['04-01-2016':'04-30-2016']
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
pred = pred.fillna(0)
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

data=df[["Precipitation"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'03-31-2016']
valid = data.loc['04-01-2016':'04-30-2016']
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
pred = pred.fillna(0)
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

data=df[["WindSpeedMax"]]
cols = data.columns
data.index = df.DATE
train = data.loc['01-01-2015':'03-31-2016']
valid = data.loc['04-01-2016':'04-30-2016']
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
pred = pred.fillna(0)
for i in range(0, len(prediction)):
       pred.iloc[i] = prediction[i]
for i in cols:
    y.append(sqrt(mean_squared_error(pred[i], valid[i])))
    print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))


###############################################################################################################################
## Threshold Values have to be tested to decide probability of forestfire based on predicted climate conditions for next 30 days
###############################################################################################################################
threshold=[ 2.553,10.595,0.943,0.654]   ####rmse values obtained while tuning parameters and testing
ff_prob=0
for i in range(0,len(threshold)):
       if y[i]>0.8*threshold[i] and y[i]<1.2*threshold[i]:
              ff_prob+=(4-i)
print("Risk of Forest Fire in next 30 days :")
if ff_prob>6:
   print ("Yes")
else:
        print("No")







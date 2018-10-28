# models

forest_fire.py: This file contains arima model,training and prediction on dehradun.csv

output.py: This is the terminal output of forest_fire.py

parameter_tuning.ipynb: This Jupyter notebook has autocorrelation plot, model summary, residual errors for 4 features - temperature, humidity, precipitation and windspeed. Autotuning of parameters for sarima model and prediction is implemented.

parameter_tuning.html: The same Jupyter notebook 'parameter_tuning.ipynb' downloaded in .html format

# azure-services

forest_fire.py script was tried executing on Azure Machine Learning Studio but it gave installation error for pyramid-arima module. This module is currently not supported by anaconda. Thus this script is run on local machine and shell output is in output.py.

parameter_tuning.ipynb notebook is run on Machine Learning Studio.

# training model

Model is trained on climatic data of past 1 year. It predicts trend for next 30 days. It calculates rmse value by comparing it with actual climatic trend of forestfire month in that region. Rmse thresholds are recorded earlier by comparing climatic trends of forest fire and non forest fire months. Comparing calculated rmse with the threshold, model predicts future occurence of forestfire.

Priority is given to the rmse of features based on their influence on forestfire and accuracy with which they are predicted.

Fine tuning of rmse values, their thresholds can be done to obtain better results.

By predicting climatic trend and forest fire occurence of a known year, and comparing it with expected actual results would give us accuracy of model.

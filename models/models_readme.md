# models

forest_fire.py: This file contains arima model,training and prediction on dehradun.csv

output.py: This is the terminal output of forest_fire.py

parameter_tuning.ipynb: This Jupyter notebook has autocorrelation plot, model summary, residual errors for 4 features - temperature, humidity, precipitation and windspeed. Autotuning of parameters for sarima model and prediction is implemented.

parameter_tuning.html: The same Jupyter notebook 'parameter_tuning.ipynb' downloaded in .html format

# azure-services

forest_fire.py script was tried to be executed on Azure Machine Learning Studio. But, it gave installation error for pyramid-arima module, which is currently not supported by anaconda. Therefore, it couldn't be executed on Azure ML Studio. Thus, this script is run on local machine and the shell output is in output.py.

parameter_tuning.ipynb notebook is run on Azure Machine Learning Studio.

# training model

Model is trained on climatic data of past 1 year. It can predict the climatic trend for the next 30 days. It calculates the rmse value by comparing it with the actual climatic trend of forestfire month in that region. The rmse thresholds are recorded earlier by comparing climatic trends of forest fire and non forest fire months. Comparing calculated rmse with the threshold, the model predicts future occurence of a forestfire.

Priority is given to the rmse of features based on their influence on forestfire and accuracy with which they are predicted.

Fine tuning of rmse values, their thresholds can be done to obtain better results.

Predicting climatic trend and forest fire occurence of a known year, and comparing it with expected actual results has given acceptable accuracy level to the model.

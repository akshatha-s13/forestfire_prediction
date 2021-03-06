# Prediction of Forest Fires: A Machine Learning and Time Series based Approach

Forest fire, a sweeping and destructive conflagration in the wilderness is one of the major causes of drastic environmental and biological changes. When human beings are exposed to gases and fine particulate matter resulting from forest fires in quantities above Permissible Exposure Limits (PEL), it results in respiratory ailments. According to a report from NASA, wildfires that occur today last for almost two months more than what they would if they had occurred back in 1970’s. Therefore, forest fires have always been a source of constant fear as they were less predictable.

Forest fire prediction constitutes a significant component of forest fire management. Hence, this project aims at predicting a forest fire prone region and the occurrence of a forest fire. Preventive measures can hence be devised to avert major catastrophes.

Though, the immediate cause for a forest fire could be an unintentional or a careless human action, extremely arid weather conditions highly contribute to the occurrence of wildfires. In this project we try to explore these weather conditions. Information regarding the climatic condition of the forest fire prone regions, i.e. temperature, humidity, precipitation, speed and direction of wind are obtained by data mining and analysed using ML techniques. Data related to the flora found in the region, density of trees, types of grasses present are also obtained. This vegetation data was not considered as they do not vary much for a partcular region and its effects could be neglected.

We intend to draw a relation between these parameters and the occurrence of a forest fire. ML algorithms such as Principal Component Analysis(PCA), Support Vector Machines(SVM), Random Forests and Gradient Boosting will be implemented along with Time Series algorithms such as ARIMA, Holt Winter’s Exponential Smoothing and Vector Auto-regression to train the multi variate model. The results of all these methods will be compared and the best suited one will be used for the test samples. Its parameters will be tweaked to have a minimum generalization error. So, given the climatic parameters of a region the proposed model will be able to predict whether a forest fire can be expected in the region, if yes, when would it occur. 

To achieve the above stated objectives, Microsoft Azure ML Studio will be employed. It provides a suitable platform to train the models faster and fine tune the parameters appropriately. It also allows to run multiple ML models in parallel and select the one which provides the most convincing results.

But, prediction alone will not suffice. Hence, we plan on deploying features to avert the disaster and minimize its impact on precious lives. The project will aim to employ thermal IR cameras at specific locations over regions where a forest fire is predicted. These sensors will be interfaced with a Raspberry Pi to communicate via a cloud service to alert (when the value crosses the set threshold) the concerned fire management authorities of the region to deploy a dense network of firefighting mechanisms over the region. The Microsoft Azure Cloud Computing platform will be used for its implementation.

Thus, the proposed project will provide a complete and efficient way to predict and prepare for forest fires.

# Folder Description

datasets : This contains the forestfire dataset which was available to us along with the dataset which we created using collected weather data.

models : This is the final folder for latest model and output.

sample-test : This folder contains the initial svm model, timeseries model and deep learning(lstm) model trained on modified uci dataset.

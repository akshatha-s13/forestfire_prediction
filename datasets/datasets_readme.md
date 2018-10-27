# Datasets

# 1.climate-data : 
Source : https://en.tutiempo.net/climate/india.html</br>
The above link was used to download climate data regionwise and monthwise.</br> 
Forest fire dates from various news reports were referred to know the dates of occurence.</br>

File names: dehradun.csv, vishakapatnam.csv</br>
Data is updated for Dehradun and Vishakapatnam.</br>

File name: imphal.csv</br>
Data collection,preprocessing and cleaning needs to be done for imphal and other regions.

Attributes:</br>
DATE,	
TempAvg,	
TempMax,	
TempMin,	
SLP,	
Humidity,	
Precipitation,	
Visibility,	
WindSpeed,	
WindSpeedMax,	
ForestFire,	
Latitude,	
Longitude,	
Altitude,	
Place


# 2.new-york
File name: new-york-state-forest-ranger-wildland-fire-reporting-database-beginning-2008.csv
This contains New York forest fire data with timestamp. This is not used for now.


# 3.uci: 
Source : kaggle<br/>
This datset was used to train initial svm model and timeseries(vector autoregression and arima) model.

File name: forestfires.csv
 
 Attribute Description:
 
 X: x-axis coordinate (from 1 to 9)<br/>
 Y: y-axis coordinate (from 1 to 9)<br/>
 month: Month of the year (January to December)<br/>
 day: Day of the week (Monday to Sunday)<br/>
 FFMC: FFMC code<br/>
 DMC: DMC code<br/>
 DC: DC code<br/>
 ISI: ISI index<br/>
 temp: Outside temperature (in ◦C)<br/>
 RH: Outside relative humidity (in %)<br/>
 wind: Outside wind speed (in km/h)<br/>
 rain: Outside rain (in mm/m2)<br/>
 area: Total burned area (in ha)<br/>

![Map of montesinho park](https://github.com/akshatha-s13/forestfire_prediction/blob/master/datasets/uci/Map%20of%20Montesinho%20natural%20park.png)

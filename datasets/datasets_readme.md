# Datasets
# 1.uci 
Source : kaggle
This datset was used to train initial svm model and timeseries(vector autoregression and arima) model.

 forestfires.csv
 
 Attribute Description
 
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

# 2.climate-data : 
Source : https://en.tutiempo.net/climate/india.html
The above link was used to download climate data regionwise and monthwise. 
Forest fire dates from various news reports were referred to know the dates of occurence.

Data is updated for Dehradun and Vishakapatnam.

Data collection,preprocessing and cleaning needs to be done for other regions.

Attributes :
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


# 3.newyork 
This contains New York forest fire data with timestamp. This is not used for now.

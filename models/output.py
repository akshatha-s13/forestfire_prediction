Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\AKSHATHA\Documents\GitHub\forestfire_prediction\models\forest_fire.py 
DATE              object
Day                int64
Month             object
Year               int64
TempAvg          float64
TempMax          float64
TempMin          float64
SLP              float64
Humidity           int64
Precipitation    float64
Visibility       float64
WindSpeed        float64
WindSpeedMax     float64
ForestFire        object
Latitude         float64
Longitude        float64
Altitude           int64
Place             object
dtype: object
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=nan, BIC=nan, Fit time=nan seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 0, 12); AIC=1826.413, BIC=1834.600, Fit time=0.224 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(1, 1, 0, 12); AIC=1741.986, BIC=1758.360, Fit time=1.995 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=1577.794, BIC=1594.168, Fit time=11.000 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 1, 12); AIC=1579.757, BIC=1600.225, Fit time=10.956 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 0, 12); AIC=1828.382, BIC=1840.663, Fit time=0.616 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 2, 12); AIC=1579.745, BIC=1600.213, Fit time=35.980 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 2, 12); AIC=1578.924, BIC=1603.485, Fit time=44.395 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 1, 12); AIC=1577.371, BIC=1589.651, Fit time=7.040 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(1, 1, 1, 12); AIC=1579.264, BIC=1595.638, Fit time=9.487 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 2, 12); AIC=1579.239, BIC=1595.613, Fit time=17.286 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(1, 1, 2, 12); AIC=1578.835, BIC=1599.302, Fit time=46.741 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(0, 1, 1, 12); AIC=1578.258, BIC=1594.632, Fit time=12.934 seconds
Total fit time: 199.108 seconds
[24.11609712 24.30179824 24.26621018 24.48615062 24.54021569 24.54431819
 24.1246145  24.21550329 24.44562939 24.32875174 24.50099219 24.29715838
 24.1119759  24.29639743 24.25952977 24.47819062 24.5309761  24.533799
 24.11281572 24.20242492 24.43127142 24.31311418 24.48407503 24.27896163
 24.09249956 24.27564149 24.23749424 24.45487549 24.50638137 24.50792468]
rmse value for TempAvg is :  2.438484256590257
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=nan, BIC=nan, Fit time=nan seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 0, 12); AIC=3303.176, BIC=3311.363, Fit time=0.186 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(1, 1, 0, 12); AIC=3220.371, BIC=3236.746, Fit time=3.477 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=3053.509, BIC=3069.883, Fit time=12.185 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 1, 12); AIC=3053.997, BIC=3074.465, Fit time=14.164 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 0, 12); AIC=3284.816, BIC=3297.097, Fit time=0.825 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 2, 12); AIC=3053.478, BIC=3073.946, Fit time=32.904 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 2, 12); AIC=nan, BIC=nan, Fit time=nan seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 2, 12); AIC=3081.690, BIC=3098.065, Fit time=15.482 seconds
Fit ARIMA: order=(0, 1, 2) seasonal_order=(0, 1, 2, 12); AIC=3024.392, BIC=3048.954, Fit time=30.922 seconds
Fit ARIMA: order=(1, 1, 3) seasonal_order=(0, 1, 2, 12); AIC=3020.245, BIC=3052.993, Fit time=60.783 seconds
Fit ARIMA: order=(1, 1, 3) seasonal_order=(1, 1, 2, 12); AIC=3019.658, BIC=3056.500, Fit time=69.231 seconds
Fit ARIMA: order=(1, 1, 3) seasonal_order=(1, 1, 1, 12); AIC=3020.829, BIC=3053.577, Fit time=27.341 seconds
Fit ARIMA: order=(1, 1, 3) seasonal_order=(0, 1, 1, 12); AIC=3021.332, BIC=3049.987, Fit time=20.964 seconds
Fit ARIMA: order=(0, 1, 3) seasonal_order=(1, 1, 2, 12); AIC=3017.705, BIC=3050.453, Fit time=57.825 seconds
Fit ARIMA: order=(0, 1, 2) seasonal_order=(1, 1, 2, 12); AIC=3023.336, BIC=3051.991, Fit time=29.059 seconds
Fit ARIMA: order=(0, 1, 3) seasonal_order=(0, 1, 2, 12); AIC=3018.280, BIC=3046.935, Fit time=49.785 seconds
Fit ARIMA: order=(0, 1, 3) seasonal_order=(2, 1, 2, 12); AIC=3019.068, BIC=3055.910, Fit time=73.207 seconds
Fit ARIMA: order=(0, 1, 3) seasonal_order=(1, 1, 1, 12); AIC=3018.872, BIC=3047.527, Fit time=25.817 seconds
Fit ARIMA: order=(0, 1, 3) seasonal_order=(0, 1, 1, 12); AIC=3019.423, BIC=3043.984, Fit time=15.711 seconds
Total fit time: 540.352 seconds
[52.60761337 52.92363337 52.83283642 50.35308783 51.21317942 51.81250477
 53.14715813 54.06726783 52.672412   54.61356941 53.59100906 51.8898832
 53.3663138  53.71370345 51.96785719 50.86084977 51.24906834 52.11599421
 53.9125791  52.90606956 52.87907652 53.02761514 51.71190006 51.47580023
 52.45037332 52.23179761 51.00671856 49.20298603 49.82910669 50.55925896]
rmse value for Humidity is :  8.81921782534171
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=3462.474, BIC=3482.942, Fit time=21.461 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 0, 12); AIC=3898.595, BIC=3906.782, Fit time=0.105 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(1, 1, 0, 12); AIC=3745.757, BIC=3762.132, Fit time=5.126 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=3460.479, BIC=3476.854, Fit time=11.830 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 1, 12); AIC=3448.759, BIC=3469.227, Fit time=24.103 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 0, 12); AIC=3582.985, BIC=3599.360, Fit time=13.998 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(1, 1, 2, 12); AIC=3451.671, BIC=3476.232, Fit time=59.145 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 0, 12); AIC=3637.423, BIC=3649.704, Fit time=3.097 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(2, 1, 2, 12); AIC=3452.824, BIC=3481.479, Fit time=64.186 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(1, 1, 1, 12); AIC=3450.534, BIC=3475.095, Fit time=21.857 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(1, 1, 1, 12); AIC=3707.063, BIC=3723.437, Fit time=9.260 seconds
Fit ARIMA: order=(0, 1, 2) seasonal_order=(1, 1, 1, 12); AIC=3450.806, BIC=3475.368, Fit time=27.016 seconds
Fit ARIMA: order=(1, 1, 2) seasonal_order=(1, 1, 1, 12); AIC=3450.371, BIC=3479.026, Fit time=17.660 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(2, 1, 1, 12); AIC=3476.360, BIC=3500.922, Fit time=18.487 seconds
Total fit time: 297.658 seconds
[-0.38775857 -0.75336788  2.43603167 -1.45424721 -1.67616521 -0.75796822
 -0.55285568 -0.85271884 -0.82171509 -1.29608722 -2.6404976   1.35075162
 -0.89870523 -1.33069265  2.42105415 -2.15896247 -2.42184587 -1.34297788
 -1.10330774 -1.45792138 -1.42315226 -1.98313786 -3.56703336  1.12837518
 -1.45205237 -1.89749698  1.95198658 -2.75173226 -3.02357847 -1.91801264]
rmse value for Precipitation is :  1.8301534008996623
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=2215.946, BIC=2236.414, Fit time=15.849 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 0, 12); AIC=2719.433, BIC=2727.620, Fit time=0.152 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(1, 1, 0, 12); AIC=2514.417, BIC=2530.791, Fit time=1.624 seconds
Fit ARIMA: order=(0, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=2219.267, BIC=2235.641, Fit time=7.275 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(1, 1, 1, 12); AIC=2217.685, BIC=2242.247, Fit time=10.177 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 0, 12); AIC=2467.611, BIC=2483.985, Fit time=5.796 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(0, 1, 2, 12); AIC=2218.126, BIC=2242.687, Fit time=24.526 seconds
Fit ARIMA: order=(1, 1, 1) seasonal_order=(1, 1, 2, 12); AIC=2219.844, BIC=2248.499, Fit time=12.417 seconds
Fit ARIMA: order=(2, 1, 1) seasonal_order=(0, 1, 1, 12); AIC=2217.819, BIC=2242.381, Fit time=7.817 seconds
Fit ARIMA: order=(1, 1, 0) seasonal_order=(0, 1, 1, 12); AIC=2364.320, BIC=2380.694, Fit time=4.390 seconds
Fit ARIMA: order=(1, 1, 2) seasonal_order=(0, 1, 1, 12); AIC=2217.654, BIC=2242.216, Fit time=26.967 seconds
Fit ARIMA: order=(0, 1, 0) seasonal_order=(0, 1, 1, 12); AIC=2454.410, BIC=2466.690, Fit time=4.326 seconds
Fit ARIMA: order=(2, 1, 2) seasonal_order=(0, 1, 1, 12); AIC=2221.373, BIC=2250.028, Fit time=13.490 seconds
Total fit time: 135.975 seconds
[4.77256562 4.94541047 4.84027706 6.61871532 5.15923165 4.80332606
 4.62298516 5.10456833 4.80278931 5.08147361 5.25073588 5.13318191
 4.79058586 4.99464109 4.89299426 6.67188864 5.21252983 4.8567129
 4.6764567  5.15812413 4.85642932 5.13519784 5.30454431 5.18707456
 4.84456272 5.04870216 4.94713953 6.72611813 5.26684353 4.91111081]
rmse value for WindSpeedMax is :  1.484041368072588
Risk of Forest Fire in next 30 days :
Yes
>>> 

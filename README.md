# Air Quality Prediction 
The Air Quality Index (AQI) is a tool used to communicate the daily air quality and its potential health effects. The AQI uses a scale of 0 to 500 to indicate how clean or polluted the air is, with higher numbers indicating worse air quality. <br>
The major contributing pollutants to India's air quality index (AQI) include: 
1. `Particulate matter (PM)`: ***PM2.5*** and PM10 are two types of particulate matter that contribute to India's AQI.
2. `Carbon monoxide (CO)`
3. `Nitrogen dioxide (NO2)`

Now, this project uses historical data from `2018-2023` and uses `PM2.5` as substitute for AQI since - 
1. The data for PM2.5 from 2018-2023 was readily available.
2. PM2.5 is one of the major contributors in AQI calculations.

Description
----
The features of this model includes - 
|S. No.| Feature Name| Symbol; Units|
|---|---|---|
|1|Average Temperature| (T; °C)|
|2|Min. Temperature| (Tm; °C)|
|3|Max. Temperature| (TM; °C)|
|4|Average relative humidity| (H; %)|
|5|Average visibility| (VV; km)|
|6|Average wind speed| (V; km/h)|
|7|	Maximum sustained wind speed| (VM; km/h)|

This model is based on `Bangalore`. The above data (features) is webscrapped from [Tutiempo](https://en.tutiempo.net/) using `Requests` library and parsed using `BeautifulSoup`. Similarly, the data for `PM2.5` (which is our output variable) is collected from [World Air Quality Historical Database](https://aqicn.org/historical/#city:india/bangalore/peenya) and it is based on the location `Peenya, Bangalore`. <br><br>

`Data Preprocessing` is done on `jupyter notebook`. <br><br>

The regression algorithms used to create the model include - 
1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regression
5. Random Forest Regression
6. XGBoost Regression

Individual Model Evaluation were performed using $R^2$, Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), $k$-cross validation. <br>
For `decision tree`, `random forest`, and `XGBoost` regression models, `hyperparamter tuning` was performed using GridSearchCV, RandomSearchCV. After every model evaluation, the model (object) is Serialized and stored in `pickle (*.pkl)` file.<br>
All models are created and evaluated in the `MODEL.ipynb` file.<br><br>

Finally, the model is presented using `Flask` library under the `app.py` python file which uses the html templates under `templates` folder and the styling is done using `css` under the  `static` folder.
The user can provide the inputs as follows - 
<div align="center">
    <img src = "Images/img2.png" width="50%"><br>
</div>

And the following page shows up on clicking the `Predict` button.<br>

<div align="center">
    <img src = "Images/img3.png" width="50%">
</div>


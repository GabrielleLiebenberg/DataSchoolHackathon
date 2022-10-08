import pandas as pd
import datetime
#from pandas import datetime

# # evaluate an ARIMA model using a walk-forward validation
# from matplotlib import pyplot
# from statsmodels.tsa.arima.model import ARIMA
# from sklearn.metrics import mean_squared_error
# from math import sqrt
# from pandas.plotting import autocorrelation_plot

# from statsmodels.tsa.stattools import adfuller
# from numpy import log
# import matplotlib.pyplot as plt
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# from statsmodels.tsa.arima_model import ARIMA


# #import pandas as pd
# import numpy as np
# from scalecast.Forecaster import Forecaster
# from pmdarima import auto_arima
# import matplotlib.pyplot as plt
# import seaborn as sns

# Importing the libraries
import numpy as np

from sklearn.model_selection import train_test_split
# Import the model we are using
from sklearn.ensemble import RandomForestRegressor



restaurant1_raw = pd.read_csv('data/orders/restaurant-1-orders.csv')
restaurant2_raw = pd.read_csv('data/orders/restaurant-2-orders.csv')
weather_raw = pd.read_csv('data/london_weather.csv')
holidays_raw = pd.read_excel('data/UK Holidays.xlsx')

weather_raw['date'] = pd.to_datetime(weather_raw['date'],format='%Y%m%d')
weather_raw['date'] = weather_raw['date'].dt.date

restaurant1_raw['Order Date'] = pd.to_datetime(restaurant1_raw['Order Date'],format='%d/%m/%Y %H:%M')
restaurant1_raw['date'] = restaurant1_raw['Order Date'].dt.date

restaurant2_raw['Order Date'] = pd.to_datetime(restaurant2_raw['Order Date'],format='%d/%m/%Y %H:%M')
restaurant2_raw['date'] = restaurant2_raw['Order Date'].dt.date

holidays_raw['date'] = pd.to_datetime(holidays_raw['date'],format='%m/%d/%Y %H:%M:%S')
holidays_raw['date'] = holidays_raw['date'].dt.date




restaurant1_temp = pd.merge(restaurant1_raw, weather_raw,
                   on = 'date',
                   how = 'inner')

restaurant1_complete = pd.merge(restaurant1_temp, holidays_raw,
                                on = 'date',
                                how='left')
        
restaurant2_temp = pd.merge(restaurant2_raw, weather_raw,
                   on = 'date',
                   how = 'inner')

restaurant2_complete = pd.merge(restaurant2_temp, holidays_raw,
                                on = 'date',
                                how='left')

agg_functions = {'Quantity': 'sum', 'Product Price': 'first', 'cloud_cover': 'first', 'sunshine': 'first', 'global_radiation': 'first', 'max_temp': 'first', 'mean_temp': 'first', 'min_temp': 'first', 'precipitation': 'first', 'snow_depth': 'first', 'isPaidTimeOff': 'first'}
#								countryOrRegion	holidayName	normalizeHolidayName	
restaurant1_avg = restaurant1_complete.groupby(['date','Item Name']).aggregate(agg_functions)
restaurant2_avg = restaurant2_complete.groupby(['date','Item Name']).aggregate(agg_functions)

#restaurant1_avg.to_csv('test.csv')

restaurant1_avg.to_csv('restaurant1_avg_data.csv')
restaurant2_avg.to_csv('restaurant2_avg_data.csv')

#machine learning code:

features = pd.read_csv('restaurant1_avg_data.csv', header=0)

# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(features)
features.fillna(0)
features[features > 1000000] = 0
features = features.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
# Labels are the values we want to predict
labels = np.array(features['Quantity'])
# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('Quantity', axis = 1)

np.nan_to_num(features)

# Saving feature names for later use
feature_list = list(features.columns)
# Convert to numpy array
features = np.array(features)


# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

print("Training Features Shape:", train_features.shape)
print("Training Labels Shape:", train_labels.shape)
print("Testing Features Shape:", test_features.shape)
print("Testing Labels Shape:", test_labels.shape)


# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
np.nan_to_num(labels)
np.nan_to_num(features)
x1 = np.where(np.isnan(train_labels))
x1 = np.where(np.isnan(train_features))
x2 = np.all(np.isfinite(train_labels))
x3 = np.where(np.isnan(train_features))
x4 = np.all(np.isfinite(train_features))
# Train the model on training data
rf.fit(features, labels);
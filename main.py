import pandas as pd
import datetime

restaurant1_raw = pd.read_csv('data/orders/restaurant-1-orders.csv')
weather_raw = pd.read_csv('data/london_weather.csv')

weather_raw['date'] = pd.to_datetime(weather_raw['date'],format='%Y%m%d')
weather_raw['date'] = weather_raw['date'].dt.date

restaurant1_raw['Order Date'] = pd.to_datetime(restaurant1_raw['Order Date'],format='%d/%m/%Y %H:%M')
restaurant1_raw['date'] = restaurant1_raw['Order Date'].dt.date
#restaurant1_raw['date'] = restaurant1_raw['date'].strftime("%d/%m/%Y")
#.strftime("%d")

#restaurant1_raw['Order Date'] = restaurant1_raw['Order Date'].strftime("%Y/%m/%d")
#3/8/2019  8:25:00 PM


output1 = pd.merge(restaurant1_raw, weather_raw,
                   on = 'date',
                   how = 'inner')
        

print(output1.head(10))
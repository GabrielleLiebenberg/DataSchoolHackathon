import pandas as pd
import datetime

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

print(restaurant2_complete.head(10))

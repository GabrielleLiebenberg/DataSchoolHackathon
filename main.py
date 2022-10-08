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

agg_functions = {'Quantity': 'sum', 'Product Price': 'first', 'cloud_cover': 'first', 'sunshine': 'first', 'global_radiation': 'first', 'max_temp': 'first', 'mean_temp': 'first', 'min_temp': 'first', 'precipitation': 'first', 'pressure': 'first', 'snow_depth': 'first', 'isPaidTimeOff': 'first'}
#								countryOrRegion	holidayName	normalizeHolidayName	
restaurant1_avg = restaurant1_complete.groupby(['date','Item Name']).aggregate(agg_functions)
restaurant2_avg = restaurant2_complete.groupby(['date','Item Name']).aggregate(agg_functions)

#restaurant1_avg.to_csv('test.csv')

restaurant1_avg.to_csv('restaurant1_avg_data.csv')
restaurant2_avg.to_csv('restaurant2_avg_data.csv')
restaurant1_complete.to_csv('restaurant1_data.csv')
restaurant2_complete.to_csv('restaurant2_data.csv')

#print(restaurant1_avg.head(10))


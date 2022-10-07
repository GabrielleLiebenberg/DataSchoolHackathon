import pandas as pd

restaurant1_raw = pd.read_csv('data/orders/restaurant-1-orders.csv')
data2 = pd.read_csv('data/london_weather.csv')


'''
output1 = pd.merge(data1, data2,
                   on = 'LOAN_NO',
                   how = 'inner')
'''        

print(data2.head(10))
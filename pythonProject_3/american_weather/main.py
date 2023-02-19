import csv
import pandas

data = pandas.read_csv("weather_data.csv")
day = data[data.day == "Monday"]
print(day)
#       day  temp condition
# 0  Monday    12     Sunny

data_dict = data.to_dict()
print(data_dict)
a = {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
     'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
     'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

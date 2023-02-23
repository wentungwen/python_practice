import csv
import pandas

weather_data = pandas.read_csv("weather_data.csv")
highest_temp = weather_data.temp.max()
weather_data_max = weather_data[weather_data.temp == highest_temp]
# print(weather_data_max)
# Monday = weather_data[weather_data.day == 'Monday']
# print(Monday.temp)
# x = Monday.temp * 1.8 + 32
# print(int(x))

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}


people_framed = pandas.DataFrame(people)
people_framed.to_csv('people_framed')



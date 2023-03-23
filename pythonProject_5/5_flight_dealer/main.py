import os

import data_manager as data_m
import flight_data as f_data
import flight_search as f_search
import notification_manager as noti_m

data_manager = data_m.DataManager()
flight_data = f_data.FlightData()
flight_search = f_search.FlightSearch()
noti_manager = noti_m.NotificationManager()

data_manager.write_to_sheety()



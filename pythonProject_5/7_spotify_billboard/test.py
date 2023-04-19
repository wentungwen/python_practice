import datetime as dt

# Example with the standard date and time format
date_str = '2023-02-28'
date_format = '%Y-%m-%d'

date_obj = dt.datetime.strptime(date_str, date_format)
user_date = dt.datetime.strftime(date_str, date_format)
print(type(date_obj))

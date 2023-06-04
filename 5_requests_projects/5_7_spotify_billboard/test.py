from datetime import datetime, timedelta


from_date = input("Which year do you want to start? YYYY-MM-DD  ")
to_date = input("Which year do you want to end with? YYYY-MM-DD  ")
start_date = datetime.strptime(from_date, "%Y-%m-%d")
end_date = datetime.strptime(to_date, "%Y-%m-%d")



def create_dates_list(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=180)
    print(dates)


create_dates_list(start_date, end_date)
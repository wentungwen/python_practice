import datetime as dt
import smtplib
import random

my_email = "wen.for.programming@gmail.com"
password = "nggfhmsfqyqiairj"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()

    msg = f"Subject: it is a cheering quote. \n\n Today's quote: {random.choice(all_quotes)}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="wentungwen@gmail.com",
            msg=msg)

date_of_birth = dt.datetime(year=1995, month=12, day=2)
print(date_of_birth)











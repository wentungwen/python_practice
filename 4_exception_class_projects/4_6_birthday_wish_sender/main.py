import datetime as dt
import random
import smtplib
import pandas as pd

PLACEHOLDER = "[NAME]"

my_email = "wen.for.programming@gmail.com"
password = "nggfhmsfqyqiairj"
now = dt.datetime.now()
date_now = f"{now.day}/{now.month}"

df = pd.read_csv("birthdays.csv")
birthday_dict = df.to_dict(orient="records")
for person in birthday_dict:
    name = person["name"]
    email = person["email"]
    day = person["day"]
    month = person["month"]
    date_birthday = f"{day}/{month}"
    if date_birthday == date_now:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as template_file:
            content = template_file.read()
            stripped_name = name.strip()
            new_content = content.replace(PLACEHOLDER, stripped_name)
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday! \n\n{new_content}")



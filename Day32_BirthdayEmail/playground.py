# import smtplib
#
# my_email = "tarsw002@gmail.com"
# password = "wjrvfuybeyywrgvl"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dbuzugbe@yahoo.co.uk",
#         msg="Subject: Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
# print(month)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995 , month=12, day=15)

import smtplib
import datetime as dt
import random


def send_email(text):
    my_email = "tarsw002@gmail.com"
    password = "wjrvfuybeyywrgvl"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dbuzugbe@yahoo.co.uk",
            msg=f"Subject: Quote of the Day\n\n{text}"
        )


# open quotes file and read to a list
with open('quotes.txt', 'r') as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

# specify day
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    send_email(quote)
    print(f"Subject: Quote of the Day\n\n{quote}")

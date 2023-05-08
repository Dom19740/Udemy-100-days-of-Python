from datetime import datetime
import pandas
import random
import smtplib
import os


# function to send email
def send_email(email, name, text):
    my_email = "tarsw002@gmail.com"
    password = "wjrvfuybeyywrgvl"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday {name}\n\n{text}"
        )
    print(f"To: {email}\n\nSubject: Happy Birthday {name}\n\n{text}")


# open csv and make list of data
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# get todays date data
now = datetime.now()
month = now.month
day_of_week = now.weekday() + 1

# search for birthday in csv matching today
for person in birthdays:

    if person["month"] == month and person["day"] == day_of_week:

        # get random letter file
        random_letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"

        # open the random letter_template
        with open(random_letter_file, mode="r") as letter_file:
            letter_template = letter_file.read()
            email_body = letter_template.replace("[NAME]", person["name"])

        # pass email, name and message to send mail function
        send_email(person["email"], person["name"], email_body)

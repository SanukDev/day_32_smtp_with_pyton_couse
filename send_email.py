import smtplib
import datetime as dt
import random


def random_quotes():
    quote_day = random.choice(list_of_quotes)
    return quote_day


now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 3:
    list_of_quotes = []
    with open("quotes.txt", "r") as data_quotes:
        list_of_data = data_quotes.readlines()
        list_of_quotes = list_of_data

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="samukakaroto123@gmail.com", password="wplk zuyj gapn ntrs")
        connection.sendmail(from_addr="samukakaroto123@gmail.com", to_addrs="samukakaroto123@gmail.com",
                            msg=f"Subject: Good morning! \n\n{random_quotes()}")

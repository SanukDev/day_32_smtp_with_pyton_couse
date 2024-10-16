# import smtplib
#
# my_email = "samukakaroto123@gmail.com"
# password = "wplk zuyj gapn ntrs"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="samukakaroto123@gmail.com", msg="Hello")
#     connection.close()
import datetime as dt

data = dt.datetime.now()
year = data.year
month = data.month
day = data.day
week_day = data.weekday()
data_of_birth = dt.datetime(year= 1994, month=8, day=6)
print(year, month, day, week_day, f"\nday of birth {data_of_birth}")
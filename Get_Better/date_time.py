import datetime

date = datetime.date(2025, 6, 25)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
time_now = datetime.datetime.now()

time_now = time_now.strftime("%H:%M:%S %Y-%m-%d")

# print(time_now)

target_datetime = datetime.datetime(2030, 1, 1, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("target date has not passed")
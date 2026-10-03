# Exercises: Day 15
# 1 Open you python interactive shell and try all the examples covered in this section.

# Exercises: Day 16
from datetime import date, datetime
# Get the current day, month, year, hour, minute and timestamp from datetime module
current = datetime.now()
print(current)
timestamps = current.timestamp
print(timestamps)
print('----------------------')

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = datetime.now()
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)
print('----------------------')

# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
data_object = datetime.strptime(date_string, "%d %B, %Y")
print(data_object)
print('----------------------')

# Calculate the time difference between now and new year.
today = date(year=2026, month=9, day=30)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)
print('----------------------')

# Calculate the time difference between 1 January 1970 and now.
today = date(year=1970, month=1, day=1)
new_year = date(year=2026, month=9, day=30)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)
print('----------------------')

# Think, what can you use the datetime module for? Examples:
print('----------------------')

# Time series analysis
print('----------------------')

# To get a timestamp of any activities in an application
print('----------------------')

# Adding posts on a blog
print('----------------------')
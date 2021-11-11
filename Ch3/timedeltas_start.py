#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date
now = datetime.now()
print(f"Today is: {now}")


# print today's date one year from now
print(f"One year from now it will be: {now + timedelta(days = 365)}")


# create a timedelta that uses more than one argument
print(f"In 2 days and 3 week, it will be: {now + timedelta(days = 2, weeks = 3)}")


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print(f"One week ago it was: {s}")

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if (afd < today):
    print("April Fool'sday already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print(f"It's just {time_to_afd.days} days until April Fool's Day")


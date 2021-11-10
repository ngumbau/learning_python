#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(f"Today's date: {today}")

  # print out the date's individual components
  print(f"Date components: day - {today.day}, month - {today.month}, year - {today.year}")
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(f"Today's weekday #: {today.weekday()}")
  days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
  print(f"Which is a: {days[today.weekday()]}")

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print(f"Current date and time: {today}")
  
  # Get the current time
  t = datetime.time(datetime.now())
  print(t)

 

  
if __name__ == "__main__":
  main();
  
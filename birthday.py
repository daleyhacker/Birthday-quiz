"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name

todaymonth = datetime.today().month
todaydate = datetime.today().day
monthname = month_name[todaymonth]
monthname = monthname.lower()


name = input("Hello, what is your name? ")

month = input("Hi "+ name + ", what was the name of the month you were born in? ")
month = month.lower()
if month == "september" or month == "october" or month =="november":
    season = "fall"
    print(season)
elif month == "december" or month == "january" or month == "february":
    season = "winter"
    print(season)
elif month == "march" or month == "april" or month == "may":
    season = "spring"
    print(season)
elif month == "june" or month == "july" or month == "august":
    season = "summer"
    print(season)


year = input("And what year were you born in, " + name + "? ")
if year >= "2000":
    decade = "two thousands"
if year == "1990" or year == "1991" or year == "1992" or year == "1993" or year == "1994" or year == "1995" or year == "1996" or year == "1997" or year == "1998" or year == "1999":
    decade = "nineties"
if year == "1980" or year == "1981" or year == "1982" or year == "1983" or year == "1984" or year == "1985" or year == "1986" or year == "1987" or year == "1988" or year == "1989":
    decade = "eighties"
if year <= "1970":
    decade = "stone age"

    print(decade)

day = input("And the day? ")

if day == "31" and month == "october":
    birthday = "You were born on Halloween!"
    print(birthday)
else:
    if day == todaydate and month == monthname:
        birthday = "Happy birthday"
        print(birthday)
    else: 
        print(name + ", you are a " + season + " baby of the " + decade + ".")
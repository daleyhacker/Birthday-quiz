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
if year == "2000" or year == "2001" or year == "2002" or year == "2003" or year == "2004" or year == "2005" or year == "2006" or year == "2007" or year == "2008" or year == "2009":
    decade = "2000s"
if year == "1990" or year == "1991" or year == "1992" or year == "1993" or year == "1994" or year == "1995" or year == "1996" or year == "1997" or year == "1998" or year == "1999":
    decade = "1990s"
if year == "1980" or year == "1981" or year == "1982" or year == "1983" or year == "1984" or year == "1985" or year == "1986" or year == "1987" or year == "1988" or year == "1989":
    decade = "1980s"
if year == "1970" or year ==  "1971" or year == "1972" or year == "1973" or year == "1974" or year == "1975" or year == "1976" or year == "1977" or year == "1978" or year == "1979":
    decade = "1970s"
if year == "1960" or year == "1961" or year == "1962" or year == "1963" or year == "1964" or year == "1965" or year == "1966" or year == "1967" or year == "1968" or year == "1969":
    decade = "1960s"
if year == "1950" or year == "1951" or year == "1952" or year == "1953" or year == "1954" or year == "1955" or year == "1956" or year == "1957" or year == "1958" or year == "1959":
    decade = "1950s"
if year == "1940" or year == "1941" or year == "1942" or year == "1943" or year == "1944" or year == "1945" or year == "1946" or year == "1947" or year == "1948" or year == "1949":
    decade ="1940s"
if year == "1930" or year == "1931" or year == "1932" or year == "1933" or year == "1934" or year == "1935" or year == "1936" or year == "1937" or year == "1938" or year == "1939":
    decade = "1930s"
if year == "1920" or year == "1921" or year == "1922" or year == "1923" or year == "1924" or year == "1925" or year == "1926" or year == "1927" or year == "1928" or year == "1929":
    decade = "1920s"
    print(decade)
day = input("And the day? ")

if day == "31" and month == "october":
    birthday = "You were born on Halloween!"
    print(birthday)

if day == "12" and month == "september":
    birthday = "Happy birthday!"
    print(birthday)
elif: 
    print(name + ", you are a " + season + " baby of the " + decade + ".")
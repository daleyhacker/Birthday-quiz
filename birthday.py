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

month = float(input("Hi "+ name + ", what was the name of the month you were born in? "))
month = month.lower() #changes everything to lower case
if month == "september" or if month == "october" or if month == "november":
    print("fall")


if month == "december" or month "january" or if month "february":
    print("winter")

if month == "march" or if month "april" or if month "may":
    print("spring")

else:
    print("summer")


year = input("And what year were you born in, " + name + "? ")
if year == "2000" or "2001" or "2002" or "2003" or "2004" or "2005" or "2006" or "2007" or "2008" or "2009":
    decade = "2000s"
if year == "1990" or "1991" or "1992" or "1993" or "1994" or "1995" or "1996" or "1997" or "1998" or "1999":
    decade = "1990s"
if year == "1980" or "1981" or "1982" or "1983" or "1984" or "1985" or "1986" or "1987" or "1988" or "1989":
    decade = "1980s"
if year == "1970" or "1971" or "1972" or "1973" or "1974" or "1975" or "1976" or "1977" or "1978" or "1979":
    decade = "1970s"
if year == "1960" or "1961" or "1962" or "1963" or "1964" or "1965" or "1966" or "1967" or "1968" or "1969":
    decade = "1960s"
if year == "1950" or "1951" or "1952" or "1953" or "1954" or "1955" or "1956" or "1957" or "1958" or "1959":
    decade = "1950s"
if year == "1940" or "1941" or "1942" or "1943" or "1944" or "1945" or "1946" or "1947" or "1948" or "1949":
    decade ="1940s"
if year == "1930" or "1931" or "1932" or "1933" or "1934" or "1935" or "1936" or "1937" or "1938" or "1939":
    decade = "1930s"
if year == "1920" or "1921" or "1922" or "1923" or "1924" or "1925" or "1926" or "1927" or "1928" or "1929":
    decade = "1920s"
    print(decade)
day = input("And the day? ")







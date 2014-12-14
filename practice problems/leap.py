#! /usr/bin/python

def leap(year):
    year = int(year)
    if ((not year % 4) and (year % 100)) or ((not year % 4) and (not year % 400)):
        print('%i is a leap year.' % (year))
    else:
        print('%i is not a leap year.' % (year))

leap(input('What year? '))

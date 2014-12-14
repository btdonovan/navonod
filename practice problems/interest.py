#! /usr/bin/python

balance = float(input('How much was borrowed? '))
apr = float(input('APR as a decimal? (e.g. 3.4% is .034) '))
mpr = apr / 12
term = int(input('What is the term of your loan in years? '))
term_m = int(term / 12)
new_bal = balance
low = newBalance / term_m
high = (balance * (1 + mpr) ** term_m) / term_m
from time import sleep
while (high - low) > 0.005:
    payment = round((low + high)/2.0, 2)
    for m in range(1, term_m + 1):
        new_bal = round(new_bal * (1 + mpr) - payment, 2)
        if new_bal < 0:
            break
    if new_bal < 0:
        high = payment
    else:
        low = payment
    print(new_bal)
    if (high - low) > 0.005:
        new_bal = balance
    sleep(0.1)
print('Result:')
print('Monthly payment to pay off debt in %s months: ', payment % (str(term_m)))

#! /usr/bin/python2

from random import random

number = int(random() * 100)
if number == 0:
    number += 1
print number
guesses = 1
guess = int(raw_input('Enter a number between 1 and 100: '))
while guess > number or guess < number:
    if guess > number:
        guess = int(raw_input('Too high. Try again: '))
        guesses += 1
    elif guess < number:
        guess = int(raw_input('Too low. Try again: '))
        guesses += 1
    else:
        guess = int(raw_input('Guess is out of range. Try again: '))
        guesses += 1
print 'Cogratulations! You got it in %i guesses.' % (guesses)

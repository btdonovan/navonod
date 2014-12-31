#! /usr/bin/python

"""
This program tracks the weight of my dogs. Since I can only weigh my dogs by weighing myself and then weighing myself holding them, it subtracts my weight from the combined weight.

The program asks for three inputs. My weight in kg. Weight with Hamish in kg. Weight with Bones in kg. It will retrieve the current date and time at runtime.

The program will output the dog's weights in kilograms and pounds.

The program writes data to a text file weights.csv. It does not record my weight since I track myself elsewhere.
"""

import datetime
date = datetime.date.today().strftime('%Y-%m-%d')
weightread = open('weights.csv', 'r')
oldweights = (weightread.readlines())[-1].split(', ')
oldweights[-1] = oldweights[-1][0:-1]
weightread.close()

holder = float(input('Enter the weight in kilograms of the person holding the dogs: '))
Hamish = float(input('Enter the combined weight of the holder and Hamish in kilograms: '))
Bones = float(input('Enter the combined weight of the holder and Bones in kilograms: '))

def dog_kg(holder, dog):
    """This function subtracts the holder's weight from the combined weight and returns the dog's weight rounded to one decimal in kilograms."""
    return round((dog - holder), 1)

def to_lbs(kgs):
    """This function returns the dog's weight in pounds rounded to one decimal."""
    return round((kgs * 2.2046), 1)

def change(new, old):
    """This function compares the dog's last recorded weight in kilograms from weights.csv to the dog's new weight and returns the change in kilograms rounded to one decimal. The returned weight is a string and is colorcoded green for a decrease and red for an increase."""
    if old >= new:
        return '\033[92mlost %s kgs.\033[0m' % (str(round((old - new), 1)))
    elif old < new:
        return '\033[91mgained %s kgs.\033[0m' % (str(round((new - old), 1)))

Hamish_old = float(oldweights[1])
Hamish = dog_kg(holder, Hamish)
Hamish_lbs = to_lbs(Hamish)
Hamish_chng = change(Hamish, Hamish_old)
Bones_old = float(oldweights[3])
Bones = dog_kg(holder, Bones)
Bones_lbs = to_lbs(Bones)
Bones_chng = change(Bones, Bones_old)

with open('weights.csv', mode='a', encoding='utf-8') as weighttable:
    weighttable.write('%s, %s, %s, %s, %s\n' % (date, Hamish, Hamish_lbs, Bones, Bones_lbs))

print('''Hamish: %s kgs, %s lbs. Hamish %s
Bones:  %s kgs, %s lbs. Bones %s''' % (Hamish, Hamish_lbs, Hamish_chng, Bones, Bones_lbs, Bones_chng))

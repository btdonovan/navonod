#! /usr/bin/python

# This program tracks the weight of my dogs. Since I can only weigh my dogs by weighing myself and then weighing myself holding them, it subtracts my weight from the combined weight.

# The program asks for three inputs. My weight in kg. Weight with Hamish in kg. Weight with Bones in kg. It will retrieve the current date and time at runtime.

# The program will output the dog's weights in kilograms and pounds.

# The program writes data to a text file weights.csv. It does not record my weight since I track myself elsewhere.

import datetime
date = datetime.date.today().strftime('%Y-%m-%d')

holder = float(input('Enter the weight in kilograms of the person holding the dogs: '))
Hamish = float(input('Enter the combined weight of the holder and Hamish in kilograms: '))
Bones = float(input('Enter the combined weight of the holder and Bones in kilograms: '))

def dog_kg(holder, dog):
    return round((dog - holder), 1)

def to_lbs(kgs):
    return round((kgs * 2.2046), 1)

Hamish = dog_kg(holder, Hamish)
Hamish_lbs = to_lbs(Hamish)
Bones = dog_kg(holder, Bones)
Bones_lbs = to_lbs(Bones)

with open('weights.csv', mode='a', encoding='utf-8') as weighttable:
    weighttable.write('%s, %s, %s, %s, %s\n' % (date, Hamish, Hamish_lbs, Bones, Bones_lbs))

print('''Hamish: %s kgs, %s lbs
Bones:  %s kgs, %s lbs''' % (Hamish, Hamish_lbs, Bones, Bones_lbs))

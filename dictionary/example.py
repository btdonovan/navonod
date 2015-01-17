#! /usr/bin/env python3

sourcedict = open('newdict.txt', 'r')
source = sourcedict.readlines()
sourcedict.close()

for i in range(len(source)):
    source[i] = source[i][0:-1]

from random import sample

def setpass():
    newpass = sample(source, 4)
    print(newpass[0], newpass[1], newpass[2], newpass[3])

setpass()

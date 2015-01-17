#! /usr/bin/env python3

fulldict = open('dict.txt', 'r')
a = True
items = fulldict.readlines()
fulldict.close()
for i in range(len(items)):
    if len(items[i]) > 4 and len(items[i]) <= 10 and "'" not in items[i]:
        with open('newdict.txt', mode='a', encoding='utf-8') as newdict:
            newdict.write(items[i])

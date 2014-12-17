#! /usr/bin/python


a = input().split()
a[0] = int(a[0])
a[1] = float(a[1])
if a[0] % 5 == 0 and a[0] <= a[1] - 0.5:
   print(a[1] - (a[0] + 0.5))
else:
   print(a[1])

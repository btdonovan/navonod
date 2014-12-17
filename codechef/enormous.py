#! /usr/bin/python
'''
a = input().split()
a[0], a[1] = int(a[0]), int(a[1])
total = 0
for i in range(a[0]):
  b = int(input())
  if b % a[1] == 0:
    total += 1
print(total)
'''
import sys
n,k,*a = map(int,sys.stdin.buffer.read().split())
total = 0
for i in a:
  if not i % k:
    total += 1
print(total)


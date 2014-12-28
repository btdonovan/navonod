#! /usr/bin/env python3
"""
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.
Input

The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.
Output

Write a single integer to output, denoting how many integers ti are divisible by k.
Example

Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
"""
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


#! /usr/bin/env python3
"""
Given the list of numbers, you are to sort them in non decreasing order.
Input

t – the number of numbers in list, then t lines follow [t <= 10^6].

Each line contains one integer: N [0 <= N <= 10^6]
Output

Output given numbers in non decreasing order.
Example

Input:

5
5
3
6
7
1

Output:

1
3
5
6
7
"""
import sys

t,*nums = map(int,sys.stdin.buffer.read().split())
nums = sorted(nums)
for i in nums:
    print(i)

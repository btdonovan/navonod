#! /usr/bin/env python3
"""
You are asked to calculate factorials of some small positive integers.

Input


An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.

Output


For each integer n given at input, display a line with the value of n!

Example
Sample input:

4
1
2
5
3

Sample output:

1
2
120
6
"""

def factorial(num):
    """Calculates the factorial of integer num."""
    nums = (i for i in range(1,num + 1))
    result = 1
    for i in nums:
        result *= i
    return result

t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))
for i in nums:
    print(factorial(i))

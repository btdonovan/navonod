#! /usr/bin/python

def factorial(num):
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

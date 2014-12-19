#! /usr/bin/python
import sys

t,*nums = map(int,sys.stdin.buffer.read().split())
nums = sorted(nums)
for i in nums:
    print(i)

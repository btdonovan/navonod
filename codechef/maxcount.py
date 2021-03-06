#! /usr/bin/env python3

"""
Given an array A of length N, your task is to find the element which repeats in A maximum number of times as well as the corresponding count. In case of ties, choose the smaller element first.
Input

First line of input contains an integer T, denoting the number of test cases. Then follows description of T cases. Each case begins with a single integer N, the length of A. Then follow N space separated integers in next line. Assume that 1 <= T <= 100, 1 <= N <= 100 and for all i in [1..N] : 1 <= A[i] <= 10000
Output

For each test case, output two space separated integers V & C. V is the value which occurs maximum number of times and C is its count.
Example

Input:
2
5
1 2 3 2 5
6
1 2 2 1 1 2

Output:
2 2
1 3

Description:
In first case 2 occurs twice whereas all other elements occur only once. 
In second case, both 1 and 2 occur 3 times but 1 is smaller than 2.
"""
import sys
T = int(sys.stdin.buffer.readline())
while T > 0:
    N = int(sys.stdin.buffer.readline())
    nums = list(map(int,sys.stdin.buffer.readline().split()))
    nums.sort(reverse=True)
    V = 0
    C = 0
    for i in nums:
        if nums.count(i) >= C:
            C = nums.count(i)
            V = i
    print(V, C)
    T -= 1

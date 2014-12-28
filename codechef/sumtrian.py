#! /usr/bin/env python3
"""
Let's consider a triangle of numbers in which a number appears in the first line, two numbers appear in the second line, three in the third line, etc. Develop a program which will compute the largest of the sums of numbers that appear on the paths starting from the top towards the base, so that:

    on each path the next number is located on the row below, more precisely either directly below or below and one place to the right;
    the number of rows is strictly positive, but less than 100
    all numbers are positive integers between O and 99.

Input

In the first line integer n - the number of test cases (equal to about 1000).
Then n test cases follow. Each test case starts with the number of lines which is followed by their content.
Output

For each test case write the determined value in a separate line.
Example

Input:
2
3
1
2 1
1 2 3
4 
1 
1 2 
4 1 2
2 3 1 1 

Output:
5
9
"""
n = int(input())
output = []
for i in range(n):
    lc = int(input())
    cl = [int(input())]

    for li in range(1, lc):
        pl = [0] + cl + [0]
        cl = list(map(lambda x, y: x + y, map(int, input().split()), map(max, pl[1:], pl[:-1])))
    output.append(max(cl)) 
for x in output:
    print(x)

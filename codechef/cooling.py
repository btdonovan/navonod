#! /usr/bin/python
'''
The chef has just finished baking several pies, and it's time to place them on cooling racks.
The chef has exactly as many cooling racks as pies. Each cooling rack can only hold one pie, and each pie may only be held by one cooling rack,
but the chef isn't confident that the cooling racks can support the weight of the pies.
The chef knows the weight of each pie,
and has assigned each cooling rack a maximum weight limit.
What is the maximum number of pies the chef can cool on the racks?
Input:

Input begins with an integer T≤30, the number of test cases.
Each test case consists of 3 lines.
The first line of each test case contains a positive integer N≤30,
the number of pies (and also the number of racks).
The second and third lines each contain exactly positive N integers not exceeding 100.
The integers on the second line are the weights of the pies, and the integers on the third line
are the weight limits of the cooling racks.
Output:

For each test case, output on a line the maximum number of pies the chef can place on the racks.
Sample input:

2
3
10 30 20
30 10 20
5
9 7 16 4 8
8 3 14 10 10
 

Sample output:

3
4

This one was fairly easy to understand. If your heaviest pie is heavier than your highest capacity rack, throw away the pie. I'm happy with my solution. Sort the pies and the racks from lightest to heaviest. Iterate from 1 to len(trays) + 1. Easy peasy.
'''

t = int(input())

for i in range(t):
    count = int(input())
    pies = list(map(int,input().split()))
    trays = list(map(int,input().split()))
    pies.sort()
    trays.sort()
    for j in range(1, len(trays) + 1):
        while len(pies) >= j and pies[-j] > trays[-j]: 
            pies.pop()
    print(len(pies))

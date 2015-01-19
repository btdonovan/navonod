#! /usr/bin/env python3

"""
In the mysterious country of Byteland, everything is quite different from what you'd normally expect. In most places, if you were approached by two mobsters in a dark alley, they would probably tell you to give them all the money that you have. If you refused, or didn't have any - they might even beat you up.

In Byteland the government decided that even the slightest chance of someone getting injured has to be ruled out. So, they introduced a strict policy. When a mobster approaches you in a dark alley, he asks you for a specific amount of money. You are obliged to show him all the money that you have, but you only need to pay up if he can find a subset of your banknotes whose total value matches his demand. Since banknotes in Byteland can have any positive integer value smaller than one thousand you are quite likely to get off without paying.

Both the citizens and the gangsters of Byteland have very positive feelings about the system. No one ever gets hurt, the gangsters don't lose their jobs, and there are quite a few rules that minimize that probability of getting mugged (the first one is: don't go into dark alleys - and this one is said to work in other places also).
Input

The first line contains integer t, the number of test cases (about 100). Then t test cases follow. Each test case starts with n, the number of banknotes in your wallet, and m, the amount of money the muggers asked of you. Then n numbers follow, representing values of your banknotes. Your wallet does not hold more than 20 banknotes, and the value of a single banknote is never more than 1000.
Output

For each test case output a single line with the word 'Yes' if there is a subset of your banknotes that sums to m, and 'No' otherwise.
Example

Input:
5
3 3
1
1
1
5 11
1
2
4
8
16
5 23
1
2
4
8
16
5 13
1
5
5
10
10
20 132 
17
6
4
998
254
137
259
153
154
3
28
19
123
542
857
23
687
35
99
999

Output:
Yes
Yes
Yes
No
Yes

 

Explanation: For example, in the last case you have to pay up, since: 6+3+123=132.

So, disapointingly this code does not run in the time allotted. This is disappointing because the code below was built based on the instructions in code chef's tutorial for this exercise. There are a number of passing submissions for this exercize that don't use the bitwise shift method posted below that ran extremely quickly (less than a second) but I'm having some difficulty groking them. (Do I get points for the gratuitous use of the word grok?)
For now, I'm leaving this alone. The code below works, it's just not fast enough to pass code chef. I seem to run into that a lot with codechef when using python3.

The sample input above has been saved to marcha1.txt and can be fed to python from bash with the following command:
    cat marcha1.txt | python3 marcha1.py
"""
#'''
import sys
t = int(sys.stdin.buffer.readline())
for h in range(t):
    n, m = map(int,sys.stdin.buffer.readline().split())
    bills = [] 
    for z in range(n):
        bills.append(int(sys.stdin.buffer.readline()))
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & 1<<j:
                sum += bills[j]
        if sum == m:
            print('Yes')
            break
    if sum != m:
        print('No')

hndrd = open('marchinput.txt', 'r')
t = int(hndrd.readline())
for h in range(t):
    n, m = map(int,hndrd.readline().split())
    bills = [] 
    found = False
    k = n
    for z in range(k):
        line = int(hndrd.readline())
        if line == m:
            found = True
            break
        if line < m:
            bills.append(line)
        if line > m:
            n -= 1
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & 1<<j:
                sum += bills[j]
        if sum == m:
            found = True
            break
    if found:
        print('Yes')
    else:
        print('No')
'''

import sys
t = int(input())
for h in range(t):
    n, m = map(int,input().split())
    bills = [] 
    found = False
    k = n
    for z in range(k):
        line = int(input())
        if line < m:
            bills.append(line)
        if line > m:
            n -= 1
        if line == m:
            found = True
    if not found:
        for i in range(1, 2 ** n):
            sum = 0
            for j in range(n):
                if i & 1<<j:
                    sum += bills[j]
            if sum == m:
                found = True
                break
    if found:
        print('Yes')
    else:
        print('No')

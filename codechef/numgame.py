#! /usr/bin/python
'''The problem tells you the players will play "optimally". There was some confusion on my part about what "optimally" meant. Optimally means they are playing to win.'''
def large():
    '''This function was when I thought "optimal" meant the players would always subtract the largest divisor of N that wasn't N. In this function I set up logic to determine the largest possible divisor by looping through numbers between 2 and N // 2 and determining if N % j == 0. If so, N = N - N % j. Other logic for dealing with 3, 2, and 1''' 
    T = int(input())
    for i in range(T):
        N = int(input())
        count = 1
        while N > 3:
            for j in range(2, (N // 2) + 1):
                if N % j == 0:
                    N = N - (N // j)
                    break
                else:
                    N -= 1
                    break
            count += 1
        if N == 3:
            count += 2
            N -= 2
        elif N == 2:
            count += 1
            N -= 1
        if count % 2 == 0:
            print('ALICE', count)
        else: print('BOB', count)

def optimal():
    '''This function assumes that the players are playing to win. In this case, players will always pass their opponent an odd number if possible. If you have an even number to start with you can always pass an odd number, but if you have an odd number to start you can only pass an even number because all divisors of odd numbers will be odd. The goal is to never pass an even number if you can avoid it. Based on this, Alice will always win if the starting number is even and Bob will always win if the starting number is odd.'''
    T = int(input())
    for i in range(T):
        N = int(input())
        if N % 2 == 0:
            print('ALICE')
        else:
            print('BOB')

import sys
def std():
    '''This function is the same as optimal() with the difference that input is gathered from stdin.'''
    t,*n = map(int,sys.stdin.buffer.read().split())
    for i in n:
        if i % 2 == 0:
            print('ALICE')
        else:
            print('BOB')

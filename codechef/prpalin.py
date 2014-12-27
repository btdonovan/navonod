#! /usr/bin/env python3
'''
 An integer is said to be a palindrome if it is equal to its
reverse. For example, 79197 and 324423 are palindromes. In this task
you will be given an integer N, 1 ≤ N ≤ 1000000. You must find
the smallest integer M ≥ N such that M is a prime number and M is a
palindrome.

For example, if N is 31 then the answer is 101.
Input

A single integer N, (1 ≤ N ≤ 1000000), on a single line.
Output

Your output must consist of a single integer, the smallest prime
palindrome greater than or equal to N.
Example

Input:
31
Output:
101
'''
def isprime(n):
    """Return True if n is a prime number. Otherwise, return False."""
    from math import sqrt
    if n != 2 and n % 2 == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, int(sqrt(n)) + 2, 2):
            if n % i == 0:
                return False
        return True

def ispalindrome(n):
    """Return True if n is a palindromic integer. Otherwise, return False."""
    if str(n) == str(n)[::-1]:
        return True

n = 98690 #int(input())
while True:
    if ispalindrome(n) and isprime(n):
        break
    else:
        n += 1
print(n)

#prpalins = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181, 18481, 19391, 19891, 19991, 30103, 30203, 30403, 30703, 30803, 31013, 31513, 32323, 32423, 33533, 34543, 34843, 35053, 35153, 35353, 35753, 36263, 36563, 37273, 37573, 38083, 38183, 38783, 39293, 70207, 70507, 70607, 71317, 71917, 72227, 72727, 73037, 73237, 73637, 74047, 74747, 75557, 76367, 76667, 77377, 77477, 77977, 78487, 78787, 78887, 79397, 79697, 79997, 90709, 91019, 93139, 93239, 93739, 94049, 94349, 94649, 94849, 94949, 95959, 96269, 96469, 96769, 97379, 97579, 97879, 98389, 98689, 1003001]

'''
prpalins = [i for i in range(2, 1003003) if i == 2 or i & 1 and ispalindrome(i) and isprime(i)]
n = 98690 #int(input())
for i in prpalins:
    if n <= i:
        print(i)
        break
'''

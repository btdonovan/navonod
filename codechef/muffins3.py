#! /usr/bin/env python3
"""
Now that Chef has finished baking and frosting his cupcakes, it's time to package them. Chef has N cupcakes, and needs to decide how many cupcakes to place in each package. Each package must contain the same number of cupcakes. Chef will choose an integer A between 1 and N, inclusive, and place exactly A cupcakes into each package. Chef makes as many packages as possible. Chef then gets to eat the remaining cupcakes. Chef enjoys eating cupcakes very much. Help Chef choose the package size A that will let him eat as many cupcakes as possible.
Input

Input begins with an integer T, the number of test cases. Each test case consists of a single integer N, the number of cupcakes.
Output

For each test case, output the package size that will maximize the number of leftover cupcakes. If multiple package sizes will result in the same number of leftover cupcakes, print the largest such size.
Constraints

    1 ≤ T ≤ 1000
    2 ≤ N ≤ 100000000 (108)

Sample Input

2
2
5

Sample Output

2
3

Explanation

In the first test case, there will be no leftover cupcakes regardless of the size Chef chooses, so he chooses the largest possible size. In the second test case, there will be 2 leftover cupcakes. 

This is a really stupid scenario. The scenario states that chef makes as many packages as possible, but then demands that we choose the package size that will allow chef to eat as many cupcakes as possible and gives the maximum package size as N. This would have been a more interesting problem if we were constrained on package size. Give the maximum leftover cupcakes given even package size between 2 and 18.

In fact, I'm going to do that now.
"""

def chef():
    """This function passes the program specifications but chef will never make more than one package of cupcakes and he will always eat slightly less than half of the available cupcakes. Chef isn't going to stay in business very long with this function."""
    t = int(input())
    for i in range(t):
        n = int(input())
        if n > 2:
            if n % 2 == 0:
                a = n + 1 - n // 2
            else:
                a = n - n // 2
        else:
            a = 2
        print(a)

def realchef():
    """This function assumes that chef will use realistic package sizes and still allows him to maximize the number of cupcakes he will eat."""
    t = int(input())
    for i in range(t):
        n = int(input())
        packages = sorted([c for c in range(2, min(n + 1, 19), 2)], reverse=True)
        remainder = []
        for j in packages:
            remainder.append(n % j)
        print(packages[remainder.index(max(remainder))], remainder[remainder.index(max(remainder))])

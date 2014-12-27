#! /usr/bin/python

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

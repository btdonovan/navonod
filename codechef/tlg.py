#! /usr/bin/python

# So the codechef problem was looking for the highest total lead at the end of any round, not the highest individual round lead. That was why it was failing before. My code was calculating the leads for individual rounds. The code below works.  The commented code below would begin just after the start of the first for loop.
n = int(input())
scores = []
L = 0
W = 0
p1=p2=0
for i in range(n):
    scores.append(input().split())
    p1 += int(scores[i][0])
    p2 += int(scores[i][1])
    if abs(p1 - p2) > L:
        L = abs(p1 - p2)
        if p1 > p2: W = 1
        else: W = 2
print(W, L)















#    for j in range(len(scores[i])):
#        scores[i][j] = int(scores[i][j])
#    if scores[i][0] > scores[i][1]:
#        scores[i].append(1)
#        L.append(scores[i][0] - scores[i][1])
#    elif scores[i][1] > scores[i][0]:
#        scores[i].append(2)
#        L.append(scores[i][1] - scores[i][0])
#print(scores[L.index(max(lead))][2], max(lead))

#! /usr/bin/python

# apparently this did not pass codechef muster. Wrong answer somewhere.
n = int(input())
scores = []
lead = []
for i in range(n):
    scores.append(input().split())
    for j in range(len(scores[i])):
        scores[i][j] = int(scores[i][j])
    if scores[i][0] > scores[i][1]:
        scores[i].append(1)
        lead.append(scores[i][0] - scores[i][1])
    elif scores[i][1] > scores[i][0]:
        scores[i].append(2)
        lead.append(scores[i][1] - scores[i][0])
print(scores[lead.index(max(lead))][2], max(lead))

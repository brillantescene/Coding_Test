import sys
from collections import deque

sys.stdin = open('Inflearn/in5.txt', 'r')

n, m = map(int, input().split())
p = deque((pos, val) for pos, val in enumerate(list(map(int, input().split()))))
t = p[m][1]
cnt = 0

while p:
    cur = p.popleft()
    if any(cur[1] < x[1] for x in p):
        p.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break

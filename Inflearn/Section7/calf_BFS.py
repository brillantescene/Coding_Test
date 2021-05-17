import sys
from collections import deque
sys.stdin = open('Inflearn/in5.txt', 'r')

MAX = 100000
check = [0]*(MAX+1)
dis = [0]*(MAX+1)
n, m = map(int, input().split())
check[n] = 1
dis[n] = 0
dq = deque()
dq.append(n)

while dq:
    x = dq.popleft()
    if x == m:
        break
    for i in [x-1, x+1, x+5]:
        if 0 < i <= MAX:
            if check[i] == 0:
                dq.append(i)
                dis[i] = dis[x]+1
                check[i] = 1
            # if i == m:
            #     print(dis[m])
            #     exit(0)
print(dis[m])

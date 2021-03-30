import sys
from collections import deque

sys.stdin = open('Inflearn/in1.txt', 'r')

n, k = map(int, input().split())
p = deque(range(1, n+1))
# p = deque(p)

while 1 < len(p):
    for _ in range(k-1):
        p.append(p.popleft())
    p.popleft()
print(p[0])

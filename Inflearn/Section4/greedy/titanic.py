import sys
from collections import deque
sys.stdin = open('Inflearn/in3.txt', 'r')

n, m = map(int, input().split())
p = list(map(int, input().split()))
# 리스트를 쓸 경우 내부 연산이 비효율적
'''
p.sort(reverse=True)
cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0]+p[-1] <= m:
        del p[0]
        del p[-1]
    else:
        del p[0]
    cnt += 1
print(cnt)
'''

p.sort(reverse=True)
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0]+p[-1] <= m:
        p.popleft()
        p.pop()
    else:
        p.popleft()
    cnt += 1
print(cnt)

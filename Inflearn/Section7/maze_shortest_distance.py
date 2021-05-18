import sys
from collections import deque

sys.stdin = open('Inflearn/in5.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = [list(map(int, input().split())) for _ in range(7)]
q = deque()
q.append((0, 0))

while q:
    tmp = q.popleft()
    if tmp[0] == tmp[1] == 6:
        break
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <= x < 7 and 0 <= y < 7:
            if not a[x][y]:
                a[x][y] = a[tmp[0]][tmp[1]] + 1
                q.append((x, y))
if not a[6][6]:
    print(-1)
else:
    print(a[6][6])

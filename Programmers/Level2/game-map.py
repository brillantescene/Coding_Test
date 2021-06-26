# 찾아라 프로그래밍 마에스터
# 게임 맵 최단거리

from collections import deque


def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append((0, 0))

    if maps[n-2][m-1] == maps[n-1][m-2] == 0:
        return -1
    while q:
        tmp = q.popleft()
        if tmp[0] == n-1 and tmp[1] == m-1:
            break
        for x1, y1 in zip(dx, dy):
            x, y = tmp[0]+x1, tmp[1]+y1
            if 0 <= x < n and 0 <= y < m:
                if maps[x][y] == 1:
                    maps[x][y] = maps[tmp[0]][tmp[1]] + 1
                    q.append((x, y))
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]

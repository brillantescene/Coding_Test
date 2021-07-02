# 11. 등산경로 DFS
'''
def dfs(n, hiking, x, y, ex, ey, ch, dx, dy):
    if x == ex and y == ey:
        return 1
    else:
        ans = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and hiking[x][y] < hiking[nx][ny] and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                ans += dfs(n, hiking, nx, ny, ex, ey, ch, dx, dy)
                ch[nx][ny] = 0
    return ans


def solution(n, hiking):
    sx = sy = 0
    ex = ey = n-1
    for i in range(n):
        for j in range(n):
            if hiking[i][j] < hiking[sx][sy]:
                sx, sy = i, j
            if hiking[i][j] > hiking[ex][ey]:
                ex, ey = i, j
    ch = [[0]*n for _ in range(n)]
    ch[sx][sy] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    return dfs(n, hiking, sx, sy, ex, ey, ch, dx, dy)


# print(solution(3, [[4, 7, 5], [5, 3, 8], [9, 6, 5]]))
# print(solution(7, [[2, 23, 92, 78, 93, 100, 34], [59, 50, 48, 90, 80, 101, 45], [30, 53, 70, 75, 96, 102, 56], [
#       94, 91, 82, 89, 93, 103, 76], [97, 98, 95, 96, 100, 104, 123], [102, 103, 104, 105, 106, 107, 23], [23, 45, 76, 34, 87, 100, 34]]))
'''

# 12. 단지 번호 붙이기

'''
def dfs(n, complex, x, y, dx, dy, cnt):
    complex[x][y] = 0
    ans = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and complex[nx][ny] == 1:
            dfs(n, complex, nx, ny, dx, dy, cnt+1)
    return cnt


def solution(n, complex):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            if complex[i][j] == 1:
                cnt = 0
                print(f"지금 complex[{i}][{j}] {complex[i][j]}")

                answer.append(dfs(n, complex, i, j, dx, dy, cnt))
                print(complex[i][j])

    return answer


print(solution(8, [[0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 0], [
      1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1]]))
# print(solution(10, [[0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 1, 0], [1, 1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], [
#       0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1]]))
'''

# 13. 섬나라 아일랜드 - BFS


'''
from collections import deque
def solution(n, maps):
    answer = 0
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, 1, -1, -1, 1]
    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                maps[i][j] = 0
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                            maps[nx][ny] = 0
                            q.append((nx, ny))

                answer += 1
    return answer


print(solution(5, [[0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [
      0, 1, 0, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0]]))
'''

# 14. 안전영역 DFS
'''
from collections import deque

def dfs(n, maps, x, y, h):
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0 and maps[nx][ny] > h:
            dfs(n, maps, nx, ny, h)

def solution(n, maps):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()

    for h in range(100):
        ch = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and maps[i][j] > h:
                    dfs(n, maps, i, j, h)

                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                                maps[nx][ny] = 0
                                q.append((nx, ny))

                    answer += 1
    return answer
    '''

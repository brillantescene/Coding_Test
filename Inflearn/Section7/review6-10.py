
# 6. 알파코드
'''
def dfs(code, res, n, level, idx):
    if level == n:
        tmp = ''
        for j in range(idx):
            tmp += chr(res[j]+64)
        return [tmp]
    else:
        ans = []
        for i in range(1, 27):
            if i == code[level]:
                res[idx] = i
                ans += dfs(code, res, n, level+1, idx+1)
            elif i >= 10 and code[level] == i // 10 and code[level+1] == i % 10:
                res[idx] = i
                ans += dfs(code, res, n, level+2, idx+1)
    return ans


def solution(code):
    n = len(code)
    res = [0]*(n+3)
    return dfs(code, res, n, 0, 0)


print(solution([2, 5, 1, 1, 4]))
'''

# 7. 송아지찾기 BFS
'''
from collections import deque


def solution(s, e):
    max = 100000
    check = [0]*(max+1)
    distance = [0] * (max+1)
    check[s] = 1
    # distance[s] = 0
    dq = deque()
    dq.append(s)

    while dq:
        x = dq.popleft()
        for i in [x-1, x+1, x+5]:
            if 0 < i <= max:
                if check[i] == 0:
                    dq.append(i)
                    distance[i] = distance[x] + 1
                    check[i] = 1
    return distance[e]


print(solution(5, 14))
'''

# 8. 사과나무 BFS
'''
from collections import deque

def solution(n, farm):
    ch = [[0]*n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((n//2, n//2))
    ch[n//2][n//2] = 1
    sum = farm[n//2][n//2]
    level = 0

    while q:
        if level == n//2:
            break
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0:
                    ch[nx][ny] = 1
                    sum += farm[nx][ny]
                    q.append((nx, ny))
        level += 1

    return sum


print(solution(7, [[74, 10, 31, 26, 59, 16, 89], [78, 44, 49, 1, 64, 33, 15], [9, 95, 70, 18, 22, 25, 40], [62, 77, 28, 3, 78, 75, 23], [82, 38, 20, 16, 42, 1, 79], [1, 24, 2, 25, 95, 26, 79], [4, 35, 46, 94, 70, 44, 83]
                   ]))
'''

# 9. 미로의 최단거리 통로 (BFS)

'''
from collections import deque

def solution(maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        if x == y == 6:
            return maze[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7 and maze[nx][ny] == 0:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
    return -1


# print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]
#                 ]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 0], [
      1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]]))
'''

# 10. 미로 탐색

'''
def dfs(maze, x, y, dx, dy):
    if x == y == 6:
        return 1
    else:
        ans = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7 and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                ans += dfs(maze, nx, ny, dx, dy)
                maze[nx][ny] = 0
    return ans


def solution(maze):
    maze[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    return dfs(maze, 0, 0, dx, dy)


print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [
      1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]]))
'''

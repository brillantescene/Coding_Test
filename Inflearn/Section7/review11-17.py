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

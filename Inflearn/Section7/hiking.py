import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(xx, yy):
    global cnt
    if xx == c and yy == d:
        cnt += 1
    else:
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if mnt[xx][yy] < mnt[x][y] and check[x][y] == 0:
                    check[x][y] = 1
                    dfs(x, y)
                    check[x][y] = 0


if __name__ == "__main__":
    n = int(input())
    mnt = [list(map(int, input().split())) for _ in range(n)]
    check = [[0]*n for _ in range(n)]
    cnt = 0
    a, b, c, d = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if mnt[i][j] < mnt[a][b]:
                a, b = i, j
            if mnt[i][j] > mnt[c][d]:
                c, d = i, j
    dfs(a, b)
    print(cnt)

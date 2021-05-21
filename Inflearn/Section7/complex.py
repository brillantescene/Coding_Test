import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(xx, yy):
    global cnt
    cnt += 1
    complex[xx][yy] = 0
    for i in range(4):
        x = xx + dx[i]
        y = yy + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if complex[x][y] == 1:
                dfs(x, y)


if __name__ == "__main__":
    n = int(input())
    complex = [list(map(int, input())) for _ in range(n)]
    res = list()
    for i in range(n):
        for j in range(n):
            if complex[i][j] == 1:
                cnt = 0
                dfs(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res:
        print(x)

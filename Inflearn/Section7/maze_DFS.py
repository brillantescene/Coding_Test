import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(lx, ly):
    global cnt

    if lx == ly == 6:
        cnt += 1
        # return
    else:
        for i in range(4):
            x = lx + dx[i]
            y = ly + dy[i]
            if 0 <= x < 7 and 0 <= y < 7 and a[x][y] == 0:
                a[x][y] = 1
                DFS(x, y)
                a[x][y] = 0


if __name__ == "__main__":
    a = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    a[0][0] = 1
    DFS(0, 0)
    print(cnt)

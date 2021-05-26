import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def dfs(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return stones[0][0]
    else:
        if x == 0:
            dy[x][y] = dfs(x, y-1) + stones[x][y]
            # return dy[x][y]
        elif y == 0:
            dy[x][y] = dfs(x-1, y) + stones[x][y]
            # return dy[x][y]
        else:
            dy[x][y] = min(dfs(x, y-1), dfs(x-1, y)) + stones[x][y]
        return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    stones = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    print(dfs(n-1, n-1))

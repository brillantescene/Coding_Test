import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = stones[0][0]
for i in range(1, n):
    dy[0][i] = stones[0][i] + dy[0][i-1]
    dy[i][0] = stones[i][0] + dy[i-1][0]
for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + stones[i][j]

print(dy[-1][-1])

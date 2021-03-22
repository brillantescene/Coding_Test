import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
n = int(input())
g = [[0]*(n+2)]*(n+2)
cnt = 0
for i in range(1, n+1):
    g[i] = list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(n):
        a = g[i][j]
        if j == 0:
            if a > g[i-1][j] and a > g[i+1][j] and a > g[i][j+1]:
                cnt += 1
        elif j == (n-1):
            if a > g[i-1][j] and a > g[i+1][j] and a > g[i][j-1]:
                cnt += 1
        else:
            if a > g[i-1][j] and a > g[i+1][j] and a > g[i][j-1] and a > g[i][j+1]:
                cnt += 1
print(cnt)

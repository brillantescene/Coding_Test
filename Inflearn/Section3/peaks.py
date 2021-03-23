import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
n = int(input())
'''
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
'''
g = [list(map(int, input().split())) for _ in range(n)]
# 가장자리 0으로 채워주기
g.insert(0, [0]*n)
g.append([0]*n)
for x in g:
    x.insert(0, 0)
    x.append(0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all() 모든 조건이 참일 때 참. 네방향 탐색 시 유용
        if all(g[i][j] > g[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)

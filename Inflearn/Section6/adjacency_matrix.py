import sys


# 그래프 그리기
sys.stdin = open('Inflearn/input.txt', 'r')

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    # 무방향
    '''
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1
    '''
    # 가중치 방향그래프
    a, b, c = map(int, input().split())
    g[a][b] = c


for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=" ")
    print()

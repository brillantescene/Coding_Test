import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

# 조합 구하기

'''
def dfs(n, m, level, start, res):
    if level == m:
        tmp = [x for x in res]
        return [tmp]
    ans = []
    for i in range(start, n+1):
        res[level] = i
        ans += dfs(n, m, level+1, i+1, res)
    return ans


def solution(n, m):
    res = [0]*m
    return dfs(n, m, 0, 1, res)


print(solution(4, 2))
'''

'''
def dfs(level, s):
    global cnt
    if level == m:
        print(*res)
        cnt += 1
        return
    for i in range(s, n+1):
        res[level] = i
        dfs(level+1, i+1)


n, m = map(int, input().split())
res = [0]*m
cnt = 0
dfs(0, 1)
print(cnt)
'''

# 수들의 조합

'''
def dfs(level, start):
    global cnt
    if level == k:
        if sum(res) % m == 0:
            cnt += 1
        return
    for i in range(start, n):
        res[level] = num[i]
        dfs(level+1, i+1)


n, k = map(int, input().split())
num = list(map(int, input().split()))
m = int(input())
res = [0] * k
cnt = 0
dfs(0, 0)
print(cnt)
'''

'''
def dfs(level, start, n, k, num, m, res):
    if level == k:
        if sum(res) % m == 0:
            return 1
        return 0
    ans = 0
    for i in range(start, n):
        res[level] = num[i]
        ans += dfs(level+1, i+1, n, k, num, m, res)
    print(f'ans {ans}')
    return ans


def solution(n, k, num, m):
    res = [0] * k
    answer = 0
    answer += dfs(0, 0, n, k, num, m, res)
    return answer


print(solution(7, 3, [2, 4, 5, 8, 12, 7, 13], 6))
'''

# 인접행렬 (가중치 방향그래프)
'''
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
'''

# 경로 탐색 (그래프 DFS)

'''
def dfs(n, m, v, ch, g):
    if v == n:
        return 1
    else:
        ans = 0
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                ans += dfs(n, m, i, ch, g)
                ch[i] = 0
    return ans


def solution(n, m, l):
    g = [[0]*(n+1) for _ in range(n+1)]

    for x in l:
        a, b = x[0], x[1]
        g[a][b] = 1

    ch = [0] * (n+1)
    ch[1] = 1
    cnt = 0
    return dfs(n, m, 1, ch, g)


print(solution(5, 9, [[1, 2], [1, 3], [1, 4], [2, 1],
                      [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]))
'''
'''
def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i)
                ch[i] = 0


n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

ch = [0] * (n+1)
ch[1] = 1
cnt = 0
dfs(1)
print(cnt)
'''

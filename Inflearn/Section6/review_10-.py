# 조합 구하기

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

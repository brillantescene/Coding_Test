# 중복 순열 구하기
'''
def dfs(level):
    global check
    if level == m:
        print(*res)
        check += 1
        return
    for i in range(1, n+1):
        res[level] = i
        dfs(level+1)


n, m = map(int, input().split())
res = [0]*m
check = 0
dfs(0)
print(check)
'''

# 동전 교환

'''
def dfs(level, sum):
    global res
    if res < level:
        return
    if sum == m:
        if level < res:
            res = level
        return
    if sum > m:
        return
    for i in range(n):
        dfs(level+1, sum+coin[i])


n = int(input())
coin = list(map(int, input().split()))
m = int(input())
coin.sort(reverse=True)
res = 2147000000
dfs(0, 0)
print(res)
'''

# 순열 구하기


def dfs(level):
    global cnt
    if level == m:
        print(*res)
        cnt += 1
        return
    for i in range(1, n+1):
        if check[i] == 0:
            check[i] = 1
            res[level] = i
            dfs(level+1)
            check[i] = 0


n, m = map(int, input().split())
res = [0]*m
check = [0]*(n+1)
cnt = 0
dfs(0)
print(cnt)

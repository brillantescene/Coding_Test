# 중복 순열 구하기
'''
def dfs(n, m, level, res):
    if level == m:
        tmp = [x for x in res]
        return [tmp]
    else:
        ans = []
        for i in range(1, n+1):
            res[level] = i
            ans += dfs(n, m, level+1, res)
    return ans


def solution(n, m):
    res = [0]*m
    return dfs(n, m, 0, res)


print(solution(3, 2))
'''

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
def dfs(n, coin, m, level, sum):

    if sum > m:
        return level

    if sum == m:
        return level

    minimum = 2147000000
    for i in range(n):
        minimum = min(minimum, dfs(n, coin, m, level+1, sum+coin[i]))
    # print(minimum, level)

    # if minimum < level:
    #     print(minimum, level)
    #     return 2147000000

    return minimum


def solution(n, coin, m):
    coin.sort(reverse=True)
    return dfs(n, coin, m, 0, 0)


# print(solution(5, [1, 8, 20, 25, 50], 129))
print(solution(3, [1, 2, 5], 15))
'''
'''
def dfs(level, sum):
    global minimum
    if minimum < level:
        return
    if sum == m:
        if level < minimum:
            minimum = level
        return
    if sum > m:
        return
    for i in range(n):
        dfs(level+1, sum+coin[i])


n = int(input())
coin = list(map(int, input().split()))
m = int(input())
coin.sort(reverse=True)
minimum = 2147000000
dfs(0, 0)
print(minimum)
'''

# 순열 구하기

'''
def dfs(n, m, level, res, ch):
    if level == m:
        tmp = [x for x in res]
        return [tmp]
    else:
        ans = []
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[level] = i
                ans += dfs(n, m, level+1, res, ch)
                ch[i] = 0
    return ans


def solution(n, m):
    res = [0]*m
    ch = [0]*(n+1)
    return dfs(n, m, 0, res, ch)


print(solution(3, 2))
'''
'''
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
'''

# 수열 추측하기

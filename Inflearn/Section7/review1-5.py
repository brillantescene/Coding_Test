# 1. 최대점수 구하기
'''
def dfs(n, m, problems, idx, score, time):
    if time > m:
        return 0
    if idx == n:
        return score
    else:
        ans = 0
        ans = max(dfs(n, m, problems, idx+1, score +
                      problems[idx][0], time+problems[idx][1]), dfs(n, m, problems, idx+1, score, time))
    return ans


def solution(n, m, problems):
    return dfs(n, m, problems, 0, 0, 0)


# print(solution(5, 20, [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]))
print(solution(9, 50, [[12, 7], [16, 8], [20, 10], [
      30, 15], [10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]))
print(solution(19, 150, [[16, 11], [20, 16], [11, 6], [5, 2], [11, 5], [12, 7], [16, 8], [20, 10], [
      30, 15], [10, 5], [25, 12], [15, 8], [6, 3], [7, 4], [3, 2], [8, 5], [9, 12], [19, 11], [9, 6]]))
'''
# 2. 휴가 (삼성 기출)

'''
def dfs(n, sch, idx, pay):
    if idx > n:
        return 0
    if idx == n:
        return pay
    else:
        ans = 0
        ans = max(dfs(n, sch, idx+sch[idx][0],
                      pay+sch[idx][1]), dfs(n, sch, idx+1, pay))
    return ans


def solution(n, sch):
    return dfs(n, sch, 0, 0)


# print(solution(5, [[3, 10], [2, 15], [1, 10], [1, 30], [2, 10]]))
print(solution(13, [[1, 20], [3, 50], [4, 30], [2, 30], [1, 10], [5, 20], [
      7, 60], [3, 20], [6, 70], [2, 30], [1, 15], [3, 50], [3, 50]]))
'''

# 3. 양팔저울
'''
def dfs(k, c, s, idx, sum):
    if idx == k:
        if sum > 0:
            return [sum]
        return [0]
    else:
        ans = []
        ans += dfs(k, c, s, idx+1, sum+c[idx])
        ans += dfs(k, c, s, idx+1, sum-c[idx])
        ans += dfs(k, c, s, idx+1, sum)
        # print(dfs(k, c, s, idx+1, sum+c[idx]))
        # print(dfs(k, c, s, idx+1, sum-c[idx]))
        # print(dfs(k, c, s, idx+1, sum))
    return ans


def solution(k, c):
    s = sum(c)
    weight = set(dfs(k, c, s, 0, 0))
    return s-len(weight)+1


# print(solution(3, [1, 5, 7]))
# print(solution(8, [1, 2, 4, 8, 16, 32, 64, 128]))
print(solution(9, [8, 13, 21, 34, 55, 89, 144, 233, 377]))
'''

# 4. 동전 바꿔주기

'''
def dfs(t, k, coin, level, sum):
    if sum > t:
        return 0
    if level == k:
        if sum == t:
            return 1
        return 0
    else:
        ans = 0
        for i in range(coin[level][1]+1):
            ans += dfs(t, k, coin, level+1, sum+(coin[level][0]*i))
    return ans


def solution(t, k, coin):
    return dfs(t, k, coin, 0, 0)


print(solution(20, 3, [[5, 3], [10, 2], [1, 5]]))
'''

# 5. 동전 분배하기

'''
# 1
def dfs(n, coin, idx, ch, a, b, c):
    if idx == n:
        if a != b and b != c and c != a and a != 0 and b != 0 and c != 0:
            return max(a, b, c) - min(a, b, c)
        return 217000000
    else:
        ans = 0
        if ch[idx] == 0:
            ch[idx] = 1
            ans = min(dfs(n, coin, idx+1, ch, a+coin[idx], b, c), dfs(
                n, coin, idx+1, ch, a, b+coin[idx], c), dfs(n, coin, idx+1, ch, a, b, c+coin[idx]))
            ch[idx] = 0
    return ans


def solution(n, coin):
    ch = [0]*n
    return dfs(n, coin, 0, ch, 0, 0, 0)
'''

'''
def dfs(n, coin, idx, money):
    if idx == n:
        sub = max(money) - min(money)
        tmp = set()
        for x in money:
            tmp.add(x)
        if len(tmp) == 3:
            return sub
        return 2147000000
    else:
        ans = 2147000000
        for i in range(3):
            money[i] += coin[idx]
            ans = min(dfs(n, coin, idx+1, money), ans)
            money[i] -= coin[idx]
    return ans


def solution(n, coin):
    money = [0]*3
    return dfs(n, coin, 0, money)


# print(solution(7, [8, 9, 11, 12, 23, 15, 17]))
# print(solution(10, [21, 34, 12, 56, 7, 8, 89, 120, 55, 77]))
print(solution(12, [11, 22, 65, 56, 78, 12, 89, 120, 55, 77, 19, 23]))
'''

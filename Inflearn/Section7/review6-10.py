# 알파코드
def dfs(code, res, n, level, idx):
    if level == n:
        tmp = ''
        for j in range(idx):
            tmp += chr(res[j]+64)
        return [tmp]
    else:
        ans = []
        for i in range(1, 27):
            if i == code[level]:
                res[idx] = i
                ans += dfs(code, res, n, level+1, idx+1)
            elif i >= 10 and code[level] == i // 10 and code[level+1] == i % 10:
                res[idx] = i
                ans += dfs(code, res, n, level+2, idx+1)
    return ans


def solution(code):
    n = len(code)
    res = [0]*(n+3)
    return dfs(code, res, n, 0, 0)


print(solution([2, 5, 1, 1, 4]))

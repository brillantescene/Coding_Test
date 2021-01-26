# 1912
# n = int(input())
# seq = list(map(int, input().split()))
# sum = [seq[0]]
# for i in range(1, n):
#     sum.append(max(sum[i-1]+seq[i], seq[i]))
# print(max(sum))

# 2579
# n = int(input())
# seq = []
# for i in range(n):
#     seq.append(int(input()))
# dp = [seq[0], seq[0]+seq[1], max(seq[0]+seq[2], seq[1]+seq[2])]
# for i in range(3, n):
#     dp.append(max(seq[i]+seq[i-1]+dp[i-3], seq[i]+dp[i-2]))
# print(dp[-1])
# why runtime error man...

# 다른 방법
# n = int(input())
# seq = [0 for _ in range(300)]
# dp = [0 for _ in range(300)]
# for i in range(n):
#     seq[i] = int(input())
# dp[0] = seq[0]
# dp[1] = seq[0]+seq[1]
# dp[2] = max(seq[0]+seq[2], seq[1]+seq[2])
# for i in range(3, n):
#     dp[i] = max(seq[i]+seq[i-1]+dp[i-3], seq[i]+dp[i-2])
# print(dp[n-1])

# 1699
# 비쥬얼코드에선 잘되는디 백준에선 (RecursionError) 발생;
def dp(n):
    count = 0
    if n in [1, 2, 3]:
        return memo[n]
    while n != 0:
        if n >= 9:
            n -= 9
            count += 1
            dp(n)
        elif n >= 4:
            n -= 4
            count += 1
            dp(n)
        else:
            count += n
            n = 0
    return count


memo = [0, 1, 2, 3]
print(dp(int(input())))

# import sys
# sys.setrecursionlimit(10**6)
# 이거 추가하면 시간 초과 발생,,
# 나중에 다시한다;

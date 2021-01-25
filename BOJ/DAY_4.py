# 210125 MON

# 1463
# def make_1(x):
#     if x in memo:
#         return memo[x]
#     y = 1 + min(make_1(x//2) + x % 2, make_1(x//3) + x % 3)
#     return y
# memo = {1: 0, 2: 1}
# print(make_1(int(input())))

# 11726
# n = int(input())
# tile = [0, 1, 2]
# for i in range(3, n+1):
#     tile.append(tile[i-1] + tile[i-2])
# print(tile[n] % 10007)

# 11727
# n = int(input())
# tile = [0, 1, 3]
# for i in range(3, n+1):
#     tile.append(2*tile[i-2] + tile[i-1])
# print(tile[n]%10007)

# 11057
# n = int(input())
# up = [0, 10, 55]
# for i in range(3, n+1):
#     up.append(int(up[i-1]*up[i-2]//2-up[i-1]))
# print(up[n]%10007)
# 답은 제대로 나오는데 시간초과 뜸
# 다른 답
# up = [[1] * 10 for _ in range(n+1)]
# for i in range(1, n):
#     for j in range(1, 10):
#         up[i][j] = up[i][j-1] + up[i-1][j]
# print(sum(up[n-1]) % 10007)

# 2193
# n = int(input())
# pinary = [1, 1]
# for i in range(2, n):
#     pinary.append(pinary[i-1]+pinary[i-2])
# print(pinary[n-1])

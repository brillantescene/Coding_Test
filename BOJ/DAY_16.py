# 210208 MON
# 11576
# a, b = map(int, input().split())
# l = list(map(int, input().split()))
# d, p = 0, 0
# r = []
# for i in l[::-1]:
#     d += i*(a**p)
#     p += 1
# while d:
#     r.append(d % b)
#     d //= b
# print(*r)

# 1978
# n = int(input())
# input()
# num = list(map(int, input().split()))
# c = 0
# for i in num:
#     if i == 0 or i == 1:
#         c += 1
#     else:
#         for j in range(2, i):
#             if i % j == 0:
#                 c += 1
#                 break
# print(len(num)-c)

# 1929
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if not num % i:
                return False
        return True


m, n = map(int, input().split())
for i in range(m, n+1):
    if isPrime(i):
        print(i)

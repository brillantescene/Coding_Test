# 210206 SAT
# 2745
# import sys
# n, b = sys.stdin.readline().split()
# n = list(n)
# b = int(b)
# n.reverse()
# for i in range(len(n)):
#     tmp = int(n[i]) if n[i].isdigit() else ord(n[i]) - 55
#     n[i] = tmp * (b**i)
# print(sum(n))

# 11005
# import sys
# n, b = map(int, sys.stdin.readline().split())
# result = []
# while n >= b:
#     result.append(n % b if n % b < 10 else chr(n % b + 55))
#     n = n // b
# result.append(n if n < 10 else chr(n + 55))
# result.reverse()
# print(''.join(map(str, result)))

import sys
n, b = map(int, sys.stdin.readline().split())
res = ''
while n > 0:
    n, r = divmod(n, b)
    res = str(r) + res if r < 10 else chr(r+55) + res
print(res)

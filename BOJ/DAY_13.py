# 210205
# 10430
# a, b, c = map(int, input().split())
# print(f"{(a+b) % c}\n{((a % c)+(b % c)) % c}\n{(a*b) % c}\n{((a % c)*(b % c)) % c}")

# 2609
# def gcd(a, b):
#     while b > 0:
#         tmp = b
#         b = a % b
#         a = tmp
#     return a

# a, b = map(int, input().split())
# print(f"{gcd(a, b)}\n{(a*b)//gcd(a, b)}")

# 라이브러리 사용
# import math
# a, b = map(int, input().split())
# print(f"{math.gcd(a,b)}\n{(a*b)//math.gcd(a,b)}")

# 1934
# def gcd(a, b):
#     if not b:
#         return a
#     return gcd(b, a % b)


# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     print((a*b)//gcd(a, b))

# 1850
import math
a, b = map(int, input().split())
print(math.gcd(a, b))

# 210215 MON
# 10872
n = int(input())
res = 1
for i in range(2, n+1):
    res *= i
print(res)

# 1676
res = 1
c = 0
for i in range(2, int(input())+1):
    res *= i
for i in str(res)[::-1]:
    if i == '0':
        c += 1
    else:
        break
print(c)

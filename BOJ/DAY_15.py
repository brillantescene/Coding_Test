# 210207 SUN
# 1373
# b = list(input())
# b.reverse()
# o = 0
# for i in range(len(b)):
#     o += int(b[i]) * (2 ** i)
# print(format(o, 'o'))
# 시간초과맨

# 2089
n = int(input())
res = ''
if n:
    while n:
        if n % (-2):
            res = '1' + res
            n = n // (-2) + 1
        else:
            res = '0' + res
            n = n // (-2)
else:
    res = 0
print(res)

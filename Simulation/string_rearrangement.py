string = input()
res = list()
num = 0
for s in string:
    if s.isalpha():
        res.append(s)
    else:
        num += int(s)
res.sort()

if num != 0:
    res.append(str(num))

print(''.join(res))
# print(*res)

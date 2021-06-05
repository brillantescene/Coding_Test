# 왕실의 나이트
x, y = map(str, input())

x = ord(x)-ord('a')+1
y = int(y)

direction = [(-2, -1), (-2, 1), (2, -1), (2, 1),
             (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0

for d in direction:
    tx = x + d[0]
    ty = x + d[1]
    if 0 < tx <= 8 and 0 < ty <= 8:
        cnt += 1

print(cnt)

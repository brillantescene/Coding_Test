import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
s = list(map(int, input().split()))

tmp = []
res = ''
l, r = 0, n-1
last = 0
while l <= r:
    if s[l] > last:
        tmp.append((s[l], 'L'))
    if s[r] > last:
        tmp.append((s[r], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            l += 1
        else:
            r -= 1
    tmp.clear()
print(len(res))
print(res)

import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def Check(cap):
    sum = 0
    cnt = 1
    for x in s:
        if sum+x > cap:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
s = list(map(int, input().split()))

maxx = max(s)
l = 1
r = sum = sum(s)
res = 0

while l <= r:
    mid = (l+r)//2
    if mid >= maxx and Check(mid) <= m:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)

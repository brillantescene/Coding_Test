import sys
sys.stdin = open('Inflearn/in2.txt', 'r')


def Check(d):
    cnt = 1
    start = 1
    while True:
        for i in range(start, n):
            tmp = s[i] - s[i-1]
            if tmp >= 5:
                cnt += 1
                start = i+1
                break
        else:
            break
    return cnt


n, c = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
l = 1
r = s[-1]
res = 0
while l <= r:
    mid = (l+r)//2
    print(Check(mid))
    if Check(mid) < c:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)

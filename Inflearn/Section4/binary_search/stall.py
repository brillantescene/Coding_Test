import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def Check(d):
    cnt = 1
    '''
    start = 0
    while True:
        for i in range(start+1, n):
            tmp = s[i] - s[start]
            if tmp >= d:
                cnt += 1
                start = i
                break
        else:
            break
    '''
    ep = s[0]
    for i in range(1, n):
        if s[i]-ep >= d:
            cnt += 1
            ep = s[i]
    return cnt


n, c = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
l = 1
r = s[-1]
res = 0
while l <= r:
    mid = (l+r)//2
    if Check(mid) >= c:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)

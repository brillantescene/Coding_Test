import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
k, n = map(int, input().split())
wire = [int(input()) for _ in range(k)]
wire.sort()
l = 1
r = wire[-1]
res = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for x in wire:
        cnt += x//mid
    if cnt >= n:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)

'''
def Count(len):
    cnt = 0
    for x in wire:
        cnt += x//len
    return cnt
'''

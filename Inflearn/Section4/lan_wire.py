import sys
sys.stdin = open('Inflearn/in1.txt', 'r')
k, n = map(int, input().split())
wire = [int(input()) for _ in range(k)]
wire.sort()


def binary_search(s, e):
    mid = (e+s)//2
    cnt = 0
    for x in wire:
        cnt += x//mid
    if cnt < n:
        binary_search(mid+1, e)
        binary_search(s, mid-1)
    if cnt >= n:
        return mid
    return 0


binary_search(1, wire[-1])

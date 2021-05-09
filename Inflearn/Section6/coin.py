import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L, sum):
    global res
    if res < L:
        return
    if m < sum:
        return
    if m == sum:
        if L < res:
            res = L
        # return
    else:
        for i in coin:
            DFS(L+1, sum+i)


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    coin.sort(reverse=True)
    res = 2147000000
    DFS(0, 0)
    print(res)

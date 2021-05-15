import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L):
    global res
    if L == n:
        sub = max(money) - min(money)
        if sub < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = sub
        return
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    money = [0]*3
    res = 2147000000
    DFS(0)
    print(res)

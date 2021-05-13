import sys
sys.stdin = open("Inflearn/in1.txt", "r")


def DFS(L, sum):
    global res
    if L == n+1:
        if res < sum:
            res = sum
        return
    else:
        if L+t[L] <= n+1:
            DFS(L+t[L], sum+p[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    t = [0]*(n+1)
    p = [0]*(n+1)
    res = -1
    for i in range(1, n+1):
        t[i], p[i] = map(int, input().split())
    print(p)
    DFS(1, 0)
    print(res)

import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L, sum):
    if L == k:
        if 0 < sum <= s:
            res.add(sum)
        return
    else:
        DFS(L+1, sum+g[L])
        DFS(L+1, sum-g[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    k = int(input())
    g = list(map(int, input().split()))
    s = sum(g)
    res = set()
    DFS(0, 0)
    print(s-len(res))

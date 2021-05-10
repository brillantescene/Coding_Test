import sys
sys.stdin = open('Inflearn/in1.txt', 'r')


def DFS(L, sum):
    if L == n and sum == f:
        print(*res)
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if not check[i]:
                res[L] = i
                check[i] = 1
                DFS(L+1, sum + (res[L]*b[L]))
                check[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * n
    b = [1] * n
    check = [0]*(n+1)
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)

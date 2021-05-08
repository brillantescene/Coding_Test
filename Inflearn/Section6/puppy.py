import sys
sys.stdin = open('Inflearn/in2.txt', 'r')


def DFS(idx, sum, tsum):
    global res
    if sum + (total-tsum) < res:
        return
    if sum > c:
        return
    if idx == n:
        if res < sum:
            res = sum
    else:
        DFS(idx+1, sum+p[idx], tsum+p[idx])
        DFS(idx+1, sum, tsum+p[idx])


if __name__ == "__main__":
    c, n = map(int, input().split())
    p = [0] * n

    for i in range(n):
        p[i] = int(input())
    total = sum(p)
    res = 0
    DFS(0, 0, 0)
    print(res)

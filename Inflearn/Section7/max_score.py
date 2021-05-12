import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if res < sum:
            res = sum
        return
    else:
        DFS(L+1, sum+s[L], time+t[L])
        DFS(L+1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = [0]*n
    t = [0]*n
    for i in range(0, n):
        a, b = map(int, input().split())
        s[i] = a
        t[i] = b
    res = 0
    DFS(0, 0, 0)
    print(res)

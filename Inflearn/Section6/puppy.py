import sys
sys.stdin = open('Inflearn/in1.txt', 'r')


def DFS(idx, sum):
    global res
    if sum > c:
        return
    if idx == n:
        if res < sum:
            res = sum
    else:
        DFS(idx+1, sum+p[idx])
        DFS(idx+1, sum)


if __name__ == "__main__":
    c, n = map(int, input().split())
    p = [0] * n

    for i in range(n):
        p[i] = int(input())

    res = 0
    DFS(0, 0)
    print(res)

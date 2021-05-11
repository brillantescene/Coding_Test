import sys
sys.stdin = open('Inflearn/in1.txt', 'r')


def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
        return
    for i in range(s, n+1):
        DFS(L+1, i+1, sum+a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = [0]+list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 1, 0)
    print(cnt)

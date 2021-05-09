import sys
sys.stdin = open('Inflearn/in4.txt', 'r')
input = sys.stdin.readline  # 대량 입력 시 되게 빨라짐


def DFS(L):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
        return
    for i in range(1, n+1):
        res[L] = i
        DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)

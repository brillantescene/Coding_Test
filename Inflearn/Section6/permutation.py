import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if check[i]:
                continue
            else:
                res[L] = i
                check[i] = 1
                DFS(L+1)
                check[i] = 0
            # if x in v:
            #     continue
            # else:
            #     res[L] = x
            #     DFS(L+1, v+[x])


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [i for i in range(1, n+1)]
    res = [0]*m
    cnt = 0
    check = [0]*(n+1)
    DFS(0)
    print(cnt)

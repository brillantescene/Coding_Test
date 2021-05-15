import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
            return
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for _ in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)

import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i]:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


n = int(input())
ch = [0]*(n+1)
DFS(1)

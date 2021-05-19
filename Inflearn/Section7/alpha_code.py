import sys
sys.stdin = open('Inflearn/in1.txt', 'r')


def DFS(L, p):
    global cnt
    if L == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j]+64), end='')
        print()
        return
    else:
        for i in range(1, 27):
            if i == code[L]:
                res[p] = i
                DFS(L+1, p+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i % 10:
                res[p] = i
                DFS(L+2, p+1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0]*(n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)

import sys
sys.stdin = open("Inflearn/in5.txt", "rt")


def prime(n):
    p = [True]*n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if p[i]:
            for j in range(i+i, n, i):
                p[j] = False
    return [i for i in range(2, n) if p[i]]


n = int(input())
print(len(prime(n+1)))

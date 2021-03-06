import sys
# sys.stdin = open("Inflearn/in5.txt", "rt")

"""
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
"""

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if not ch[i]:  # ch[i]가 0이면
        cnt += 1
        for j in range(i+i, n+1, i):  # 개수 세는거라 i나 i+i나 상관없음
            ch[j] = 1
print(cnt)
print(ch)

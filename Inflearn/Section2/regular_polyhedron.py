import sys
sys.stdin = open("Inflearn/in4.txt", "rt")

n, m = map(int, input().split())
res = []

# 내 방법
# for i in range(1, 2):
#     for j in range(1, m+1):
#         res.append(i+j)
# print(*res[n-1:])

cnt = [0] * (n+m+3)
max = -2147000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
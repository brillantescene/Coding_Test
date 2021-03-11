import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        if sum == m:
            cnt += 1
            break
print(cnt)

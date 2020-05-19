n = int(input())
p = [0] + list(map(int, input().split()))
r = [0] * (n+1)
r[1] = p[1]
for i in range(2, n + 1):
    for j in range(1, i+1):
        if r[i] < r[i - j] + p[j]:
            r[i] = r[i - j] + p[j]
print(r[n])
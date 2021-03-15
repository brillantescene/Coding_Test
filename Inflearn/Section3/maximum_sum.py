import sys
sys.stdin = open("Inflearn/in1.txt")

n = int(input())
grid = [[]]*n
res = []
sum3, sum4 = 0, 0
max = 0
for i in range(n):
    grid[i] = list(map(int, input().split()))
for i in range(n):
    sum1, sum2 = 0, 0
    for j in range(n):
        sum1 += grid[i][j]
        sum2 += grid[j][i]
    sum3 += grid[i][i]
    sum4 += grid[i][n-1-i]
    res.append(sum1)
    res.append(sum2)
res.append(sum3)
res.append(sum4)

# print(max(res))
for x in res:
    if max < x:
        max = x
print(max)

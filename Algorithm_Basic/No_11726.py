tiling = [0, 1, 2]
for i in range(3, 1001):
  tiling.append(tiling[i - 2] + tiling[i - 1])
n = int(input())
print(tiling[n] % 10007)
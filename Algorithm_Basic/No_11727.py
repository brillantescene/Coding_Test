tiling = [0, 1, 3]
for i in range(3, 1001):
  tiling.append(2 * tiling[i - 2] + tiling[i - 1])
n = int(input())
print(tiling[n] % 10007)
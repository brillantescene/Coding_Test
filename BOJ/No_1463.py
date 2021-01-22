n = int(input()) + 1
min_cnt = [-1 for i in range(n)]
for i in range(1, n):
    min_cnt[i] = min_cnt[i-1] + 1
    if i % 2 == 0:
        min_cnt[i] = min([min_cnt[i], min_cnt[int(i/2)]+1])
    if i % 3 == 0:
        min_cnt[i] = min([min_cnt[i], min_cnt[int(i/3)]+1])

print(min_cnt[-1])
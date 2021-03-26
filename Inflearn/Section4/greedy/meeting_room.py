import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]

meet.sort(key=lambda x: x[1])
'''
res = [meet[0]]
idx = 0
for i in range(1, n):
    if meet[i][0] >= res[idx][1]:
        res.append(meet[i])
        idx += 1
print(len(res))
'''

et = cnt = 0
for s, e in meet:
    if s >= et:
        et = e
        cnt += 1
print(cnt)

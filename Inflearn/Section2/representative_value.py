import sys
sys.stdin = open("Inflearn/in1.txt", "rt")
n = int(input())
score = list(map(int, input().split()))
mean = round(sum(score)/n)

# gap = abs(mean - score[0])
# res = {}
# for i in range(1, n):
#     if abs(mean - score[i]) < gap:
#         gap = abs(mean - score[i])
#         res[gap] = i+1
# print(mean, res[min(res)])

min = 2147000000
for i, x in enumerate(score):
    gap = abs(mean - x)
    if gap < min:
        min = gap
        score = x
        res = i + 1
    elif gap == min:
        if x > score:
            score = x
            res = i + 1
print(mean, res)

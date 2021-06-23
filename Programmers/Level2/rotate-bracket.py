# 월간 코드 챌린지 시즌 2
# 약수의 개수와 덧셈

# def solution(s):
#     answer = -1
#     return answer

from collections import defaultdict


def solution(v):
    answer = []
    v.sort()
    x = defaultdict(int)
    y = defaultdict(int)

    for coor in v:
        x[coor[0]] += 1
        y[coor[1]] += 1

    for x, y in zip(x, y):
        print(x, y)
    return


print(solution([[1, 4], [3, 4], [3, 10]]))

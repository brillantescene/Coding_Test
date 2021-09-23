def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    a = set(lottos) & set(win_nums)
    print(a)
    return [rank[len(a)], rank[len(a)+zero]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

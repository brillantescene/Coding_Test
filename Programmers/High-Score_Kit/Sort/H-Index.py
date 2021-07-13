# def solution(citations):
#     citations.sort()
#     h = len(citations)

#     for i in range(h):
#         if citations[i] >= h-i:
#             return h-i
#     return 0


def solution(citations):
    citations.sort(reverse=True)
    # answer = max(map(min, enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))
    return 0


# print(solution([3, 0, 6, 1, 5]))
print(solution([4, 7, 0, 2, 3, 0, 6, 1, 5]))

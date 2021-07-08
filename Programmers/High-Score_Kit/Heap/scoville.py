import heapq as hq


def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        hq.heappush(scoville, (hq.heappop(scoville) + hq.heappop(scoville)*2))
        answer += 1
    if scoville[0] < K:
        return -1

    return answer


# print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1, 1, 1, 1, 1, 1, 1], 26))
# print(solution([0, 0, 3, 9, 10, 12], 7000))
print(solution([0, 0, 3, 9, 10, 12], 0))
print(solution([0, 0, 3, 9, 10, 12], 1))

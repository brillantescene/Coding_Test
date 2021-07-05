from collections import deque


def solution(priorities, location):
    q = deque([(idx, p) for idx, p in enumerate(priorities)])
    answer = 0

    while q:
        j = q.popleft()
        if any(j[1] < x[1] for x in q):
            q.append(j)
        else:
            answer += 1
            if j[0] == location:
                return answer


print(solution([2, 1, 3, 2],	2))

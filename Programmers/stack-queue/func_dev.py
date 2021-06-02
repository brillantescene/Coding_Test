# 기능개발
from collections import deque


def solution(progresses, speeds):
    answer = []
    cnt = 0
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for i in range(len(progresses)):
            if progresses[i] >= 100:
                cnt += 1
            else:
                break

        for _ in range(cnt):
            progresses.popleft()
            speeds.popleft()

        if cnt != 0:
            answer.append(cnt)
            cnt = 0

    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([99, 1, 99, 1], [1, 1, 1, 1]))
# print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))
print(solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]))
# print(solution([99, 99, 99], [1, 1, 1]))
# print(solution([96, 99, 98, 97], [1, 1, 1, 1]))

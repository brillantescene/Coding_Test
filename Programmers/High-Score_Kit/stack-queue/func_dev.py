# 기능개발

# 이렇게 하면 O(n^2)
'''
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
'''
# 반복문 한 번만 쓰기 ~


def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0] < -((p-100)//s):
            answer.append([-((p-100)//s), 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]

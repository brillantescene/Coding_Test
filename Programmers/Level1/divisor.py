# 월간 코드 챌린지 시즌 2
# 약수의 개수와 덧셈
import math


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        # print(i**0.5, i**0.5)
        if i**0.5 == i**0.5:
            answer -= i
        else:
            answer += i
    return answer


print(solution(13, 17))
print(solution(24, 27))

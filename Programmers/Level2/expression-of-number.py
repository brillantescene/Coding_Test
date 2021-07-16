# 연습문제
# 숫자의 표현

def solution(n):
    answer = 1
    for i in range(n//2+1, 0, -1):
        sum = 0
        x = i
        while x > 0:
            sum += x
            x -= 1
            if sum > n:
                break
            if sum == n:
                answer += 1
                break
        if x <= 0:
            return answer
    return answer


def solution(n):
    answer = 1
    for i in range(1, n//2+2):
        sum = 0
        while sum < n:
            sum += i
            i += 1
            if sum == n:
                answer += 1
                break
    return answer

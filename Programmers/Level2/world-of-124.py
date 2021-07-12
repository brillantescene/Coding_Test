# 연습 문제
# 124 나라의 숫자

# 내가 푼 방법
def solution(n):
    answer = ''
    num = ['4', '1', '2']
    while n:
        answer = num[n % 3] + answer
        if n % 3 == 0:
            n = (n-1)//3
        else:
            n = n//3
    return answer

# if 쓰지 않는 풀이


def change124(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

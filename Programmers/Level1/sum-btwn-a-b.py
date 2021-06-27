# 연습문제
# 두 정수 사이의 합

def solution(a, b):
    return sum(range(a, b+1)) or sum(range(b, a+1))

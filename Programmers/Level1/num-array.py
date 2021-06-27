# 연습문제
# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    return sorted([a for a in arr if a % divisor == 0]) or [-1]

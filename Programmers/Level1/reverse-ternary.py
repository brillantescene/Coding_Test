# 월간 코드 챌린지 시즌 1
# 3진법 뒤집기

# int 함수 이용하기
def solution(n):
    answer = 0
    ternary = ''
    while n:
        ternary += str(n % 3)
        n = n // 3
    return int(ternary, 3)


'''
def solution(n):
    answer = 0
    ternary = ''
    while n:
        ternary = str(n % 3) + ternary
        n = n // 3
    for i in range(len(ternary)):
        answer += int(ternary[i]) * (3**i)
    return answer
'''

print(solution(125))

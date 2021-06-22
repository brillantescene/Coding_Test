# 월간 코드 챌린지 시즌 1
# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += s.count('0')
        # 0 제거
        s = s.replace('0', '')
        # s길이를 이진법으로
        s = bin(len(s))[2:]

        answer[0] += 1
    # answer[1] += s.count('0')
    # s = s.replace('0', '')
    # s = bin(len(s))[2:]
    # print(s)
    return answer


print(solution("110010101001"))

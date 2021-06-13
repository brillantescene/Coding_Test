# 2018 카카오 공채 1차
# 다트게임

def solution(dartResult):
    answer = 0
    result = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if result and dartResult[i-1].isdigit():
                result[-1] = result[-1]*10+int(dartResult[i])
            else:
                result.append(int(dartResult[i]))
        if dartResult[i] in ['S', 'D', 'T']:
            result[-1] = result[-1] ** bonus[dartResult[i]]
        if dartResult[i] == '*':
            result[-1] = result[-1] * 2
            if len(result) > 1:
                result[-2] = result[-2] * 2
        if dartResult[i] == '#':
            result[-1] = - result[-1]
    print(result)
    return sum(result)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))

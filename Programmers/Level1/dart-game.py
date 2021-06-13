# 2018 카카오 공채 1차
# 다트게임

def solution(dartResult):
    result = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    tmp = ''
    for d in dartResult:
        if d.isdigit():
            if result and tmp.isdigit():
                result[-1] = result[-1]*10+int(d)
            else:
                result.append(int(d))
                tmp = d

        if d in ['S', 'D', 'T']:
            result[-1] = result[-1] ** bonus[d]
            tmp = ''
        if d == '*':
            result[-1] = result[-1] * 2
            if len(result) > 1:
                result[-2] = result[-2] * 2
        if d == '#':
            result[-1] = - result[-1]
    return sum(result)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))

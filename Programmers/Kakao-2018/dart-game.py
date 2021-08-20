def solution(dartResult):
    result = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    prev = 0
    for d in dartResult:
        if d.isdigit():
            if type(prev) == int and prev > 0:
                prev = prev*10 + int(d)
            else:
                prev = int(d)
        else:
            if d in ['S', 'D', 'T']:
                result.append(prev ** bonus[d])
            elif d == '*':
                result[-1] = result[-1] * 2
                if len(result) > 1:
                    result[-2] = result[-2] * 2
            else:
                result[-1] = - result[-1]
            prev = d
    return sum(result)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

# 월간 코드 챌린지 시즌 1
# 내적

def solution(a, b):
    # return sum([a[i]*b[i] for i in range(len(a))])
    return sum(x*y for x, y in zip(a, b))

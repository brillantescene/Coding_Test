# 월간 코드 챌린지 시즌 2
# 음양 더하기

def solution(absolutes, signs):
    answer = 0

    # for x, sign in zip(absolutes, signs):
    #     if sign:
    #         answer += x
    #     else:
    #         answer -= x

    return sum(x if sign else -x for x, sign in zip(absolutes, signs))


print(solution([4, 7, 12], [True, False, True]))

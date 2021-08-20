# 2018 카카오 공채 - 뉴스 클러스터링

import re
from collections import Counter


def solution(str1, str2):
    answer = 0
    temp1 = [str1[i:i+2].lower() for i in range(len(str1)-1)]
    temp2 = [str2[i:i+2].lower() for i in range(len(str2)-1)]

    str1_arr = []
    str2_arr = []

    while temp1:
        tmp = temp1.pop()
        if tmp.isalpha():
            str1_arr.append(tmp.lower())
    while temp2:
        tmp = temp2.pop()
        if tmp.isalpha():
            str2_arr.append(tmp.lower())

    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)

    union = intersection = 0

    for c in counter1:
        if c in counter2:
            intersection += min(counter1[c], counter2[c])
            union += max(counter1[c], counter2[c])
        else:
            union += counter1[c]
    for c in counter2:
        if not c in counter1:
            union += counter2[c]

    answer = 1 if union == 0 else intersection/union
    return int(answer*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))

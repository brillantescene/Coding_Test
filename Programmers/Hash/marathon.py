# 난 이렇게 풀었는데
# def solution(participant, completion):
#     answer = ''
#     dic = {}
#     for p in participant:
#         dic[p] = dic.get(p, 0) + 1
#     for c in completion:
#         dic[c] -= 1
#     for k, v in dic.items():
#         if v:
#             answer = k
#     return answer

# Counter를 사용하면 엄청 간결해진다
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))

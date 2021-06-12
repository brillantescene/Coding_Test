# 2019 카카오 개발자 겨울 인턴십
# 튜플
def solution(s):
    answer = []
    prev = ''
    tmp = []
    cnt = 0
    left = right = 0
    result = {}
    for ch in s:
        if ch in ['{', ',']:
            prev = ch
        if ch.isdigit():
            if prev.isdigit():
                tmp[-1] = tmp[-1]*10 + int(ch)
                prev = ch
            if prev in ['{', ',']:
                tmp.append(int(ch))
                prev = ch
                cnt += 1
        if ch == '}' and prev.isdigit():
            right += cnt
            answer.append(tmp[left: right])
            left += cnt
            cnt = 0
            prev = ch

    answer.sort(key=lambda x: len(x))

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            result[answer[i][j]] = 0

    return list(result.keys())


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))

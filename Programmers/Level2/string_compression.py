# 2020 KAKAO BLIND RECRUITMENT
# 문자열 압축

def solution(s):
    answer = 2147000000
    n = len(s)

    for i in range(1, n//2):
        tmp = s[0:i]
        cnt = 1
        res = ''
        for j in range(i, n+1, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)+tmp
                else:
                    res += tmp
                cnt = 1
                tmp = s[j:j+i]
        if n % i != 0:
            res += s[n-(n % i):]
        if len(res) == 0:
            break
        answer = min(len(res), answer)
        print(i, res, answer)
    return answer


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))

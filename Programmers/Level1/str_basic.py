import re


def solution(s):
    print(len(s))
    if len(s) == 4 or len(s) == 6:
        if re.search("[^0-9]", s):
            print(s)
            return False
        else:
            return True
    return False


print(solution("1234"))
print(solution("a234"))

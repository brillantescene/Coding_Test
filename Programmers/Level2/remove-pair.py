# 2017 팁스타운
# 짝지어 제거하기

def solution(s):
    stack = []
    if len(s) % 2 != 0:
        return 0
    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

    return 0 if stack else 1

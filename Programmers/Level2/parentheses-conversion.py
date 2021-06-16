# u, v 나누기
def seperate(string):

    left = right = 0
    u = v = ''
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = string[:i+1]
            v = string[i+1:]
            break
    return u, v

# 올바른 괄호인지


def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack

# u 뒤집기


def reverse(u):
    return ''.join([')' if s == '(' else '(' for s in u])


def recursive(string):
    # 1
    if not string:
        return string
    # 2
    u, v = seperate(string)

    if is_correct(u):
        return u + recursive(v)  # 3
    else:
        return '(' + recursive(v) + ')' + reverse(u[1:-1])  # 4


def solution(p):
    return p if is_correct(p) else recursive(p)


print(solution('()))((()'))

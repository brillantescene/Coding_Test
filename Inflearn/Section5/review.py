# 2. 쇠막대기
'''
def solution(pipe):
    answer = 0
    stack = []

    for p in pipe:
        if p == '(':
            stack.append(p)
        else:
            if prev == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
        prev = p
    return answer


print(solution('()(((()())(())()))(())'))
print(solution('(((()(()()))(())()))(()())'))
print(solution('(((()(()()))(())()))(()())(((()(()()))(())()))(()())'))
print(solution('(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))'))
'''
# 3. 후위 표기식 만들기

'''
def solution(infix):
    postfix = []
    op = []

    for x in infix:
        if x.isdigit():
            postfix.append(x)
        else:
            if op:
                if x in ['+', '-']:
                    while op and op[-1] in ['+', '-', '*', '/']:
                        postfix.append(op.pop())
                    op.append(x)

                elif x in ['*', '/']:
                    while op and op[-1] in ['*', '/']:
                        postfix.append(op.pop())
                    op.append(x)

                elif x == '(':
                    op.append(x)

                else:
                    while True:
                        if op[-1] == '(':
                            op.pop()
                            break
                        else:
                            postfix.append(op.pop())
            else:
                op.append(x)

    while op:
        postfix.append(op.pop())
    return postfix


# print(solution('(3+5)*2'))
# print(solution('3*(5+2)-9'))
# print(solution('5+7*3-5+(3+2*3)'))
# print(solution('5+8+6*5-(3+2)-7*3-5+(3+2*3)'))
print(solution('5+8+6*5-(3+2)-7*3-5+(3+2*3)+(5+3+2-5*2)+3'))
'''

# 4. 후위식 연산


def solution(postfix):
    stk = []
    for x in postfix:
        if x in ['+', '-', '*', '/']:
            a = stk.pop()
            b = stk.pop()
            if x == '+':
                stk.append(b+a)
            elif x == '-':
                stk.append(b-a)
            elif x == '*':
                stk.append(b*a)
            else:
                stk.append(b/a)
        else:
            stk.append(x)
    return stk[0]


# print(solution([3, 5, 2, '+', '*', 9, '-']))
print(solution([5, 7, 3, '*', '+', 5, '-', 3, 2, 3, '*', '+', '+']))
# print(solution(''))
# print(solution(''))

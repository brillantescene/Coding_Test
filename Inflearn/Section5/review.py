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

'''
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
'''

# 5. 공주구하기

'''
from collections import deque

def solution(n, k):
    q = deque([i for i in range(1, n+1)])

    cnt = 0
    while len(q) > 1:
        cnt += 1
        if cnt == k:
            q.popleft()
            cnt = 0
        else:
            q.append(q.popleft())
    return q[0]


# print(solution(8, 3))
# print(solution(20, 3))
print(solution(1000, 9))
'''

# 6. 응급실
'''
from collections import deque

def solution(m, p):
    q = deque([(idx, x) for idx, x in enumerate(p)])
    cnt = 0
    while q:
        patient = q.popleft()
        if any(patient[1] < x[1] for x in q):
            q.append(patient)
        else:
            if patient[0] == m:
                return cnt+1
            else:
                cnt += 1


# print(solution(2, [60, 50, 70, 80, 90]))
# print(solution(5, [63, 53, 87, 91, 83, 72,
#                    83, 92, 63, 68, 88, 74, 51, 82, 89]))
print(solution(0, [60, 60, 90, 60, 60, 60]))
'''

# 7. 교육과정 설계

'''
from collections import deque
def solution(ness, plan):
    answer = []
    for p in plan:
        n = deque(ness)
        print(p)
        for x in p:
            if x in n:
                if x == n[0]:
                    n.popleft()
                else:
                    answer += ['NO']
                    break
        else:
            if not n:
                answer += ['YES']
            else:
                answer += ['NO']
    return answer


# print(solution(['C', 'B', 'A'], ['CBDAGE', 'FGCDAB', 'CTSBDEA']))
# print(solution(['A', 'K', 'D', 'E', 'F'], ['AYKGDHEJ',
#                                            'AQKWDERTFYP', 'CTFKSBDEA', 'ASKGHDEF', 'WOPASFKGHDEF']))
'''

# 8. 단어찾기


def solution(words, poem):
    # dic = {}
    # for word in words:
    #     dic[word] = 0
    # for p in poem:
    #     dic[p] = 1

    for word in words:
        if word not in poem:
            return word

    # return [x for x in dic if not dic[x]]


print(solution(['big', 'good', 'sky', 'blue', 'mouse'],
               ['sky', 'good', 'mouse', 'big']))

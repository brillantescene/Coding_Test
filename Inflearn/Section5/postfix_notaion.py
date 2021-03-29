import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

a = list(input())
res = ''
op = []
op_dic = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}

for x in a:
    print(f"x {x}")
    if x.isdigit():
        res += x
    else:
        if x == '(':
            op.append(x)
        elif x == '*' or x == '/':
            while op and (op[-1] == '*' or op[-1] == '/'):
                res += op.pop()
            op.append(x)
        elif x == '+' or x == '-':
            while op and (op[-1] != '('):
                res += op.pop()
            op.append(x)
        elif x == ')':
            while op and (op[-1] != '('):
                res += op.pop()
            op.pop()

while op:
    res += op.pop()
print(res)

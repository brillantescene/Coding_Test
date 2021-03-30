import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

a = list(input())
res = ''
op = []

for x in a:
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

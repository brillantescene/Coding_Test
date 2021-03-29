import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

p = list(input())
stack = []
for x in p:
    if x.isdigit():
        stack.append(int(x))
    else:
        b = stack.pop()
        a = stack.pop()
        if x == '+':
            stack.append(a+b)
        elif x == '-':
            stack.append(a-b)
        elif x == '*':
            stack.append(a*b)
        elif x == '/':
            stack.append(a/b)
print(stack[0])

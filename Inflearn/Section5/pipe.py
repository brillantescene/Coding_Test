import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

p = list(input())
stack = []
pre = ''
cnt = 0
for x in p:
    if x == '(':
        stack.append(x)
    else:
        stack.pop()
        if pre == '(':
            cnt += len(stack)
        else:
            cnt += 1
    pre = x
print(cnt)

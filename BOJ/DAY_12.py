# 210204 THU
# 1406
# 시간 초과를 해결해보자 !
import sys
stack_l = list(sys.stdin.readline())
stack_l = stack_l[:-1]
n = int(input())
stack_r = []
for _ in range(n):
    com = sys.stdin.readline().split()
    if 'P' in com:
        stack_l.append(com[1])
    elif 'B' in com and stack_l:
        stack_l.pop()
    elif 'L' in com and stack_l:
        stack_r.append(stack_l.pop())
    elif 'D' in com and stack_r:
        stack_l.append(stack_r.pop())
stack_r.reverse()
print(''.join(stack_l+stack_r))
# list 두 개, sys 사용! -> \n 제거해주기

# 1158
n, k = map(int, input().split())
seq = [i for i in range(1, n+1)]
x = k-1
res = []
for _ in range(n):
    if x >= len(seq):
        x = x % len(seq)
    res.append(seq.pop(x))
    x += k-1
print('<'+', '.join(map(str, res))+'>')

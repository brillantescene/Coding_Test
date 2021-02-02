# 210202 TUE
# 1406
import sys
line = list(sys.stdin.readline())
n = int(input())
c = len(line)
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if c:
            c -= 1
    elif cmd[0] == 'D':
        if c < len(line):
            c += 1
    elif cmd[0] == 'B':
        if c:
            del line[c-1]
            c -= 1
    else:
        line.insert(c, cmd[1])
        c += 1
print(''.join(line))
# 내일은 시간 초과 문제를 해결해보자,,

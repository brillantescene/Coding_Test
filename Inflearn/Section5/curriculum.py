import sys
from collections import deque

sys.stdin = open('Inflearn/in2.txt', 'r')

com = input()

for i in range(int(input())):
    curri = input()
    dq = deque(com)
    for x in curri:
        if x in dq:
            if x != dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        print(f"#{i+1} NO" if dq else f"#{i+1} YES")

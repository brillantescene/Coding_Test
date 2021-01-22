import sys
while True:
    str = sys.stdin.readline().rstrip('\n')
    if not str:
        break
    print(len(str))
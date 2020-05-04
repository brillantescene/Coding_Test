import sys
while True:
    str = sys.stdin.readline().rstrip('\n')
    result = [0, 0, 0, 0]
    
    if not str:
        break
    for ch in str:
        if ch.islower():
            result[0] += 1
        elif ch.isupper():
            result[1] += 1
        elif ch.isdigit():
            result[2] += 1
        else:
            result[3] += 1

    for result in result:
        print(result, end=" ")
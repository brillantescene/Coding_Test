t = int(input())

for _ in range(t):
    left, right = 0, 0
    testdata = input()
    for i in range(len(testdata)):
        if testdata[i] == '(':
            left += 1
        elif testdata[i] == ')':
            right += 1
        if left == right:
            left, right = 0, 0
        elif left > right:
            continue
        else:
            break
    if left == 0 and right == 0:
        print("YES")
    else: print("NO")

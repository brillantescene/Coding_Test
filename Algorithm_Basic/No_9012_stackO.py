def isVPS(string):
    stack = []
    for i in string:
        if len(stack) == 0 and i == ')':
            return "NO"
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"

    return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        testdata = input().strip()
        print(isVPS(testdata))

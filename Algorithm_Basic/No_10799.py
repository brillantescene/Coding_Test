def howManyPieces(string):
    stack = []
    pieces = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        else:
            if string[i-1] == '(':
                stack.pop()
                pieces += len(stack)
            else:
                stack.pop()
                pieces += 1
    return pieces

if __name__ == "__main__":
    pipe = list(input())
    print(howManyPieces(pipe))
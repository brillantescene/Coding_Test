sentence = list(input())
count = int(input())
pointer = len(sentence)
stack = []
for i in len(sentence):
    stack[i] = sentence[i]

for _ in range(count):
    order = list(input())
    if len(order) == 1:
        if order[0] == 'L':
            if pointer == 0:
                pointer = 0
            else:
                pointer -= 1
        elif order[0] == 'D':
            if pointer == len(sentence):
                pointer = len(sentence)
            else:
                pointer += 1
        elif order[0] == 'B':
            if pointer == 0:
                continue
            else:
                tmp = pointer
                for _ in range(len(sentence)-pointer):
                    stack[pointer-1] = stack[pointer]
                    pointer += 1
                pointer = tmp
    else:
        i = 1
        for i in range(len(sentence)-pointer+1):
            stack[len(sentence)] = 
        stack[pointer] =


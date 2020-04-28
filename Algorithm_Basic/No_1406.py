import sys
input = sys.stdin.readline

sentence = list(input().strip())
count = int(input())
cursor = len(sentence)

for _ in range(count):
    order = list(input())
    if order[0] == 'L':
        if cursor == 0:
            continue
        else:
            cursor -= 1
    elif order[0] == 'D':
        if cursor == len(sentence):
            continue
        else:
            cursor += 1
    elif order[0] == 'B':
        if cursor == 0:
            continue
        else:
            del(sentence[cursor-1])
            cursor -= 1
    elif order[0] == 'P':
        sentence.insert(cursor, order[2])
        cursor += 1

print("".join(sentence))
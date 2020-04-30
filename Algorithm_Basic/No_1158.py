import sys
input = sys.stdin.readline

n, k = map(int, input().split())

queue = [i for i in range(1, n + 1)]
josephus = "<"

while(True):
    for _ in range(k - 1):
        queue.append(queue.pop(0))
    josephus += str(queue.pop(0))
    if len(queue) == 0:
        break
    else:
        josephus += ", "

print(josephus + ">")
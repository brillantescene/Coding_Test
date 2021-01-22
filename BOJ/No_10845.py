import sys
input = sys.stdin.readline

class queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            return -1
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def front(self):
        if self.empty():
            return -1
        return self.items[0]

    def back(self):
        if self.empty():
            return -1
        return self.items[-1]


count = int(input())
que = queue()

while count > 0:
    count -= 1
    x = input().split()
    order = x[0]
    if order == 'push':
        que.push(int(x[1]))
    elif order == 'pop':
        print(que.pop())
    elif order == 'size':
        print(que.size())
    elif order == 'empty':
        print(int(que.empty()))
    elif order == 'front':
        print(que.front())
    elif order == 'back':
        print(que.back())
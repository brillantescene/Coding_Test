import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def top(self):
        if self.empty():
            return -1
        return self.items[-1]


count = int(input())
stk = stack()

while count > 0:
    count -= 1
    x = input().split()
    order = x[0]
    if order == 'push':
        stk.push(int(x[1]))
    elif order == 'pop':
        print(stk.pop())
    elif order == 'size':
        print(stk.size())
    elif order == 'empty':
        print(int(stk.empty()))
    elif order == 'top':
        print(stk.top())
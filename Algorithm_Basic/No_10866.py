import sys
input = sys.stdin.readline

class deque:
    def __init__(self):
        self.items = []
    def push_front(self, item):
        self.items.insert(0, item)
    def push_back(self, item):
        self.items.append(item)
    def pop_front(self):
        if self.empty():
            return -1
        return self.items.pop(0)
    def pop_back(self):
        if self.empty():
            return -1
        return self.items.pop()
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

deq = deque()
count = int(input())

for _ in range(count):
    x = input().split()
    order = x[0]
    if order == 'push_front':
        deq.push_front(x[1])
    elif order == 'push_back':
        deq.push_back(x[1])
    elif order == 'pop_front':
        print(deq.pop_front())
    elif order == 'pop_back':
        print(deq.pop_back())
    elif order == 'size':
        print(deq.size())
    elif order == 'empty':
        print(int(deq.empty()))
    elif order == 'front':
        print(deq.front())
    elif order == 'back':
        print(deq.back())

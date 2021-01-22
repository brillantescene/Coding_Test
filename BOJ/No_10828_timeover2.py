class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()

    def isEmpty(self):
        return not self.items


count = int(input())
stk = stack()
for _ in range(count):
    order = input().split()
    if order[0] == 'push':
        stk.push(int(order[1]))
    elif order[0] == 'pop':
        print(stk.pop())
    elif order[0] == 'size':
        print(len(stk.items))
    elif order[0] == 'empty':
        if stk.isEmpty():
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if stk.isEmpty():
            print(-1)
        else:
            print(stk.items[-1])
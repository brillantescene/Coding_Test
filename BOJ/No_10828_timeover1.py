count = int(input())
list_x = []

for _ in range(count):
    order = input().split()
    if order[0] == 'push':
        list_x.append(int(order[1]))
    elif order[0] == 'pop':
        if not list_x:
            print(-1)
        else:
            print(list_x[-1])
            list_x.pop()
    elif order[0] == 'size':
        print(len(list_x))
    elif order[0] == 'empty':
        if not list_x:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if not list_x:
            print(-1)
        else:
            print(list_x[-1])
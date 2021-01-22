time = int(input())

for i in range(time):
    a, b = map(int, input().split())
    print("Case #%d: %d"%(i+1, a+b))
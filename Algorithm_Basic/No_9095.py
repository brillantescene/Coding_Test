t = int(input())

for _ in range(t):
    n = int(input())
    s = [0, 1, 2, 4]
    for i in range(4, 12):
        s.append(s[i-3]+s[i-2]+s[i-1])
    print(s[n])
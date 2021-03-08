import sys
sys.stdin = open("Inflearn/in1.txt", "rt")
'''
n = int(input())
arr = [[]]*n
res = []
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2]:
        tmp = 10000+arr[i][0]*1000
    elif arr[i][0] == arr[i][1] or arr[i][0] == arr[i][2]:
        tmp = 1000+arr[i][0]*100
    elif arr[i][1] == arr[i][2]:
        tmp = 1000+arr[i][1]*100
    else:
        tmp = max(arr[i])*100
    res.append(tmp)

print(max(res))
'''
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()  # 3 1 3
    tmp.sort()  # 1 3 3 -> 맨 뒤가 제일 큼
    a, b, c = map(int, tmp)
    if a == b and b == c:
        m = 10000+a*1000
    elif a == b or a == c:
        m = 1000+a*100
    elif b == c:
        m = 1000+b*100
    else:
        m = c*100
    if m > res:
        res = m
print(res)

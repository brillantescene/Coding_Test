import sys
sys.stdin = open('Inflearn/in4.txt', 'r')
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0]*(n+1)
dy[1] = 1
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and max < dy[j]:
            max = dy[j]
    dy[i] = max+1
    if dy[i] > res:
        res = dy[i]
print(res)

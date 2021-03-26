import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
'''
p.sort(key=lambda x: x[1])
cnt = 0

for i in range(n):
    for j in range(n):
        if p[i][1] < p[j][1]:
            if p[i][0] < p[j][0]:
                break
    else:
        cnt += 1
print(cnt)
'''
largest = cnt = 0
p.sort(reverse=True)
for h, w in p:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)

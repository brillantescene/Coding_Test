import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

n = int(input())
ans = list(map(int, input().split()))
'''
res = []
for i in range(len(ans)):
    if ans[i] == 0:
        res.append(0)
    elif i != 0 and ans[i] == 1 and res[i-1] != 0:
        res.append(res[i-1]+1)
    else:
        res.append(1)
print(sum(res))
'''
sum = 0
cnt = 0
for x in ans:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)

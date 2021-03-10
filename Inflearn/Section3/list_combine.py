import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
# print(*sorted(list1+list2))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if list1[p1] <= list2[p2]:
        c.append(list1[p1])
        p1 += 1
    else:
        c.append(list2[p2])
        p2 += 1
if p1 < n:
    c += list1[p1:]
if p2 < m:
    c += list2[p2:]
print(*c)

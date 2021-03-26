import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

n = int(input())
w = list(map(int, input().split()))
m = int(input())
w.sort()
for _ in range(m):
    w[-1] -= 1
    w[0] += 1
    w.sort()
print(w[-1]-w[0])

# import sys
# sys.stdin = open("Inflearn/in5.txt", "rt")
t = int(input())
for i in range(1, t+1):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    print(f"#{i} {sorted(num[s-1:e])[k-1]}")

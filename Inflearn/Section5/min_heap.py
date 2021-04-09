import sys
import heapq as hq

sys.stdin = open('Inflearn/in1.txt', 'r')
a = []
index = 1
while True:
    x = int(input())
    if x == -1:
        break
    if not x:
        if a:
            print(hq.heappop(a))  # 루트 노드 값 pop
        else:
            print(-1)
    else:
        hq.heappush(a, x)  # 리스트 a에 x값 push
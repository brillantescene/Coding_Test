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
            print(-hq.heappop(a))  # 루트 노드 값 pop
        else:
            print(-1)
    else:
        # 기본적으로 최소힙으로 동작되기 때문에 최대힙 효과를 내기 위해서 음수로 바꾸자
        hq.heappush(a, -x)

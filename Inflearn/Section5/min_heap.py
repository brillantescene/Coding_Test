import sys
'''
sys.stdin = open('Inflearn/in3.txt', 'r')
heap = [0]
index = 1
while True:
    x = int(input())
    if x == -1:
        break
    if not x and heap:
        print(heap.pop(1))
        index -= 1
    else:
        heap.append(x)
        childIndex = index
        parentIndex = childIndex//2
        while True:
            if heap[parentIndex] > heap[childIndex]:
                tmp = heap[parentIndex]
                heap[parentIndex] = heap[childIndex]
                heap[childIndex] = tmp
            childIndex = parentIndex
            parentIndex = childIndex // 2
            if parentIndex == 0:
                break
        index += 1
'''
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

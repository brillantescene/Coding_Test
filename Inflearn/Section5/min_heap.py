import sys
from collections import deque

# sys.stdin = open('Inflearn/in1.txt', 'r')
heap = deque()
index = 0
while True:
    x = int(input())
    print(f"전 heap {heap}")
    if x == -1:
        break
    if not x and heap:
        print(heap.popleft())
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
    print(f"후 heap {heap} index {index}")
print(heap)

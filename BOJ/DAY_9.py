# 210131 SUN
# 10845
# from collections import deque
# import sys
# n = int(input())
# queue = deque([])
# for i in range(n):
#     command = list(sys.stdin.readline().split())
#     if 'push' in command:
#         queue.append(command[1])
#     elif 'pop' in command:
#         print(queue.popleft() if queue else -1)
#     elif 'size' in command:
#         print(len(queue))
#     elif 'empty' in command:
#         print(1 if not queue else 0)
#     elif 'front' in command:
#         print(queue[0] if queue else -1)
#     else:
#         print(queue[-1] if queue else -1)

# 10866
# from collections import deque
# import sys
# n = int(input())
# deq = deque([])
# for _ in range(n):
#     com = list(sys.stdin.readline().split())
#     if 'push_front' in com:
#         deq.appendleft(com[1])
#     elif 'push_back' in com:
#         deq.append(com[1])
#     elif 'pop_front' in com:
#         print(deq.popleft() if deq else -1)
#     elif 'pop_back' in com:
#         print(deq.pop() if deq else -1)
#     elif 'size' in com:
#         print(len(deq))
#     elif 'empty' in com:
#         print(1 if not deq else 0)
#     elif 'front' in com:
#         print(deq[0] if deq else -1)
#     else:
#         print(deq[-1] if deq else -1)

# 10808
word = input()
alpha = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
for i in word:
    alpha[i] += 1
for i in alpha.keys():
    print(alpha[i]), end = ' ')

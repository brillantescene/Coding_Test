# 210129 FRI
# 10989
# import sys
# n = int(input())
# nums = [0]*10001
# for _ in range(n):
#     nums[int(sys.stdin.readline())] += 1
# for i in range(10001):
#     if nums[i] != 0:
#         for j in range(nums[i]):
#             print(i)
# 출력에서 이것도 괜찮네
# for i in range(1, 10001):
#     print(f'{i}\n' * nums[i], end='')

# 11652
# import sys
# n = int(input())
# cards = {}
# for i in range(n):
#     tmp = int(sys.stdin.readline())
#     if tmp in cards:
#         cards[tmp] += 1
#     else:
#         cards[tmp] = 1
# cardlist = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
# print(cardlist[0][0])

# 11004
# import sys
# n, k = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
# print(sorted(a)[k-1])

# 10828
# import sys
# n = int(input())
# stack = []
# for _ in range(n):
#     command = list(sys.stdin.readline().split())
#     if 'push' in command:
#         stack.append(command[1])
#     elif 'pop' in command:
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif 'size' in command:
#         print(len(stack))
#     elif 'empty' in command:
#         print(0 if stack else 1)
#     else:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)

# 9012
# t = int(input())
# for _ in range(t):
#     stack = []
#     tmp = input()
#     for i in tmp:
#         if i == '(':
#             stack.append(i)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#     if stack:
#         print('NO')
#     else:
#         print('YES')

# 10799
pipe = input()
stack = []
cnt = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append(pipe[i])
    else:
        stack.pop()
        if pipe[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)

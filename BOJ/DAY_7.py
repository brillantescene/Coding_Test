#
# 11651
# import sys
# n = int(input())
# coor = []
# for _ in range(n):
#     coor.append(list(map(int, sys.stdin.readline().split())))
# coor.sort(key=lambda x: (x[1], x[0]))
# for i in coor:
#     print(i[0], i[1])

# 10814
# import sys
# n = int(input())
# user = []
# for _ in range(n):
#     user.append(list(sys.stdin.readline().split()))
# user.sort(key=lambda x: int(x[0]))
# for i in user:
#     print(i[0], i[1])

# 이렇게 해서 틀렸다
# user.sort(key=lambda x: x[0])
# 차이가 뭐지,,?

# 10825
# import sys
# n = int(input())
# students = []
# for _ in range(n):
#     students.append(list(sys.stdin.readline().split()))
# students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# for i in students:
#     print(i[0])

# 10989
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# for i in sorted(nums):
#     print(i)
# 메모리 초과 떠부렀삼
# sys로 변경
import sys
n = int(input())
nums = [0]*10001
for i in range(n):
    nums[i] = int(sys.stdin.readline())
for i in sorted(nums):
    if i != 0:
        print(i)

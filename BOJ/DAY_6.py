# 210127 WED
# 2751
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# for i in sorted(nums):
#     print(i)
# 시간 초과 ~^^
# sys로 해봤다
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))
# 이렇게 바꿨더니 1432ms 나왔다,, 넘 느려
# import sys
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))
# for i in sorted(nums):
#     sys.stdout.write(str(i)+'\n')
# 이렇게 하면 1400ms,,

# 11650
# import sys
# n = int(input())
# coor = []
# for _ in range(n):
#     coor.append(list(map(int, sys.stdin.readline().split())))
# for i in sorted(coor):
#     sys.stdout.write(str(i[0])+' '+str(i[1])+'\n')

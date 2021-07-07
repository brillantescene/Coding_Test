# 가장 큰 수

def solution(nums, m):
    stack = []

    for num in nums:
        while stack and m > 0 and stack[-1] < num:
            stack.pop()
            m -= 1
        stack.append(num)

    if m != 0:
        stack = stack[:-m]
    return stack


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
# print(solution([9, 8, 7, 6, 5, 4, 3, 2, 1], 3))

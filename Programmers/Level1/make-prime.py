import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i]+nums[j]+nums[k]
                cnt = cnt + 1 if is_prime(sum) else cnt
    return cnt

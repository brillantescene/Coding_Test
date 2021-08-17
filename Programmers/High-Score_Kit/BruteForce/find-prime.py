# 완전탐색 level 2 소수찾기

from itertools import permutations
import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    result = []
    for i in range(1, len(numbers)+1):
        permutation = list(map(''.join, permutations(list(numbers), i)))
        result += map(int, permutation)

    for num in set(result):
        if isPrime(num):
            answer += 1
    return answer


print(solution("011"))

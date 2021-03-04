import sys
sys.stdin = open("Inflearn/in5.txt", "rt")


def digit_sum(digit):
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit = digit // 10
    # for x in str(digit):
    #     sum += int(x)
    return sum


int(input())
nums = list(map(int, input().split()))

max = -2147000000
for x in nums:
    sum = digit_sum(x)
    if max < sum:
        max = sum
        res = x

print(res)

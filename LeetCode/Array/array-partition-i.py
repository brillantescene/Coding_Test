
# 내 방법
def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += min(nums[i], nums[i+1])
    return sum

# min 하지 않아도 짝수 애들이 더 작음. sort 했으니까


def arrayPairSum2(nums):
    nums.sort()
    sum = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum

# arrayPairSum2()를 파이썬답게 코딩하면?


def arrayPairSum3(nums):
    return sum(sorted(nums)[::2])


print(arrayPairSum3([6, 2, 6, 5, 1, 2]))

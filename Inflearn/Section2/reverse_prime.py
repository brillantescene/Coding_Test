import sys
sys.stdin = open("Inflearn/in5.txt", "rt")

n = int(input())
num = list(map(int, input().split()))


def reverse(x):
    res = ''
    while x > 0:
        res += str(x % 10)
        x = x // 10
    return int(res)


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if not (x % i):
            return False
    return True


for x in num:
    y = reverse(x)
    if isPrime(y):
        print(y, end=" ")

import sys
sys.stdin = open("Inflearn/in5.txt", "rt")

n = int(input())
num = list(map(int, input().split()))


def reverse(x):
    '''
    문자열 사용
    res = ''
    while x > 0:
        res += str(x % 10)
        x = x // 10
    return int(res)
    '''
    # 숫자 사용
    res = 0
    while x > 0:
        t = x % 10
        res = res*10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if not (x % i):
            return False
    else:
        return True


for x in num:
    y = reverse(x)
    if isPrime(y):
        print(y, end=" ")

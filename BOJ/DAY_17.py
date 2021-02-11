# 210211 THU
# 6588
import sys


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True


while True:
    n = int(sys.stdin.readline())
    if n > 4:
        a, b = 0, 0
        for i in range(n, 0, -1):
            if isPrime(i):
                b = i
                a = n-b
                if isPrime(a):
                    break
                else:
                    continue
        print(f"{n} = {n-b} + {b}")
    elif 0 < n and n <= 4:
        print("Goldbach's conjecture is wrong.")
    else:
        break

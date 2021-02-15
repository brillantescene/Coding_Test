# 210212
# 11653
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True


n = int(input())
c = n
res = []
while True:
    if n == 1:
        break
    if isPrime(n):
        res.append(n)
        break
    for i in range(2, c):
        if isPrime(i):
            if n % i == 0:
                res.append(i)
                n = n // i
            else:
                continue
res.sort()
print('\n'.join(map(str, res)))
# 시간 초과. 다음에 다시 할 것!

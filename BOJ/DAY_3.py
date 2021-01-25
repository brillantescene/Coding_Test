# 210124 SUN

# 2442
n = int(input())
for i in range(n, 0, -1):
    print(' '*(i-1)+'*'*(2*(n-i)+1))

# 2445
n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print('*'*i+' '*(2*(n-i))+'*'*i)
    else:
        print('*'*(2*n-i)+' '*(2*(i-n))+'*'*(2*n-i))

# 다른 방법! 이게 더 빠르다
n = int(input())
for i in range(1, n):
    print('*'*i+' '*(2*(n-i))+'*'*i)
for i in range(n, 0, -1):
    print('*'*i+' '*(2*(n-i))+'*'*i)

# 2446
n = int(input())
for i in range(n-1):
    print(' '*i+'*'*(2*(n-i)-1))
for i in range(n-1, -1, -1):
    print(' '*i+'*'*(2*(n-i)-1))
# 출력 형식이 잘못됐다고 뜰 땐 뒤쪽 공백을 확인하자 !

# 2522
n = int(input())
for i in range(1, n):
    print(' '*(n-i)+'*'*(i))
for i in range(n, 0, -1):
    print(' '*(n-i)+'*'*(i))

# 10991
n = int(input())
for i in range(1, n+1):
    print("*")

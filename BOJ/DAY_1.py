# 210122 FRI
# 2557
import sys
print("Hello World!")

# 1000
x, y = map(int, input().split())
print(x+y)

# 2558
x = int(input())
y = int(input())

print(x+y)

# 10950
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(x+y)

# 10951
# while 쓰면 런타임에러 뜸 -> 더 이상 입력이 없는데도 수행돼서 그런 듯.
# sys.stdin은 빈 문자열 반환

for input in sys.stdin:
    print(sum(map(int, input.split())))

# 10952

for input in sys.stdin:
    x, y = map(int, input.split())
    if not x and not y:
        break
    else:
        print(x+y)

# 10953
t = int(input())

for _ in range(t):
    x, y = map(int, input().split(','))
    print(x+y)

# 11021
# 스위프트랑 헷갈림 ㅎㅎ;;

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(f"Case #{i+1}: {x+y}")

# 11022
t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(f"Case #{i+1}: {x} + {y} = {x+y}")

# 11718

print(sys.stdin.read())

# 이렇게 간단하게 끝나다니;;
# sys.stdin에 대해 알아보자

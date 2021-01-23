# 210123 SAT

# 11719
import sys

print(sys.stdin.read())

# 11720
# 1
n = int(input())
nums = list(map(int, input()))
print(sum(nums))

# 2
sum = 0
n = int(input())
nums = list(map(int, input()))

for i in nums:
    sum += i
print(sum)

# - 두 가지 버전으로 해봤는데, sum() 함수를 안쓰는게 좀 더 빠르다 72ms, 64ms

# 다른 사람이 한 것
input()
print(sum(map(int, input())))

# - n 입력 받아봤자 안쓰니까 변수에 담지를 않았다. 호오
# - 그리고 입력하나 더 받으면서 그대로 출력해버리기! 리스트로 바꾸지도 않았네? 이거 괜찮다

# 11721
line = input()
for i in range(0, len(line), 10):
    print(line[i:i+10])

# - string으로 다 받고 10씩 띄어서 for문 돌리기 !

# 2741
n = int(input())
for i in range(1, n+1):
    print(i)

# 2742
n = int(input())
for i in range(n, 0, -1):
    print(i)
# 난 이렇게 했는데, 다른 사람걸 확인해보니 어메이징;;
n = int(input())
print("\n".join(map(str, range(n, 0, -1))))


# 2739
n = int(input())
for i in range(1, 10):
    print(f"{n} * {i} = {n*i}")

# 1924
# 딕셔너리를 써봤음
m, d = map(int, input().split())
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
sum = 0
for i in range(1, m):
    sum += month[i]
print(day[(sum+d) % 7])
# 68ms 넘 느림. 다른 사람은 딕셔너리 말고 걍 조건문 써보겠음

x, y = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i == 2:
        y += 28
    else:
        y += 30
print(day[y % 7])
# 근데 똑같이 68나옴; 머임;

x, y = map(int, sys.stdin.readline().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i == 2:
        y += 28
    else:
        y += 30
print(day[(y) % 7])
# sys를 써도 똑같네;;

# 8393
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 다른 방법
print(sum(range(int(input())+1)))

# 10818
input()
nums = list(map(int, input().split()))
min, max = nums[0], nums[0]
for i in nums:
    if i <= min:
        min = i
    if i >= max:
        max = i
print(min, max)
# 이 방법 진짜 개느리다. 500ms 나옴

# 이건 다른 방법
a, *b = map(int, sys.stdin.read().split())
print(min(b), max(b))
# 이 방법은 400ms 아니 다른 사람들껀 졸 빠르던데 내꺼 왜케 느림;

# 2438
for i in range(1, int(input())+1):
    print("*" * i)

# 2439
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*" * i)

# 2440
for i in range(int(input()), 0, -1):
    print("*"*i)

# 2441
n = int(input())
for i in range(n, 0, -1):
    print(" "*(n-i)+"*"*i)

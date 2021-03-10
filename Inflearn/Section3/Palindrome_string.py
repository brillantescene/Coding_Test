import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

n = int(input())

# 직접 구현
for i in range(n):
    pal = input().lower()
    for j in range(len(pal)//2):
        if pal[j] != pal[-1-j]:
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")

# 파이썬스럽게
for i in range(n):
    p = input().lower()
    if p == p[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

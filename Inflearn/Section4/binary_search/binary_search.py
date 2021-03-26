import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

# 재귀
'''
def binary_search(s, e):
    x = (e+s)//2
    if num[x] == m:
        print(x+1)
    elif num[x] < m:
        binary_search(x+1, e)
    elif num[x] > m:
        binary_search(s, x-1)
    else:
        return False

binary_search(0, n-1)
'''

# while

lt = 0
rt = n-1

while lt <= rt:
    mid = (lt+rt)//2
    if num[mid] == m:
        print(mid+1)
        break
    elif num[mid] < m:
        lt = mid + 1
    else:
        rt = mid - 1

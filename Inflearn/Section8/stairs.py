import sys
sys.stdin = open('Inflearn/in1.txt', 'r')


def dfs(num):
    if dy[num] > 0:
        return dy[num]
    if num == 1 or num == 2:
        return num
    else:
        dy[num] = dfs(num-1) + dfs(num-2)
        return dy[num]


if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(dfs(n))

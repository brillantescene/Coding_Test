import sys
sys.stdin = open('Inflearn/in5.txt', 'r')


def binary(x):
    if x == 1:
        print(1, end='')
    else:
        binary(x//2)
        print(x % 2, end='')


n = int(input())
binary(n)


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end='')


if __name__ == "__main__":
    n = int(input())
    DFS(n)

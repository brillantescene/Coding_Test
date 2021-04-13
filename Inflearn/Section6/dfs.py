import sys
# sys.stdin = open('Inflearn/input.txt', 'r')


def DFS(v):
    if v > 7:
        return
    else:
        # print(v, end=" ")
        DFS(v*2)  # 왼쪽 자식노드
        # print(v, end=" ")
        DFS(v*2+1)  # 오른쪽 자식노드
        print(v, end=" ")


DFS(1)

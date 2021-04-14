import sys

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ") # 전위순회
        DFS(v*2)  # 왼쪽 자식노드
        # print(v, end=" ") # 중위순회
        DFS(v*2+1)  # 오른쪽 자식노드
        # print(v, end=" ") # 후위순회

DFS(1)
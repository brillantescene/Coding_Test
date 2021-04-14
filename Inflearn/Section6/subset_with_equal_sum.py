import sys
sys.stdin = open('Inflearn/in4.txt', 'r')


def DFS(index, sum):
    if sum > total//2:  # 시간복잡도를 줄여보자
        return
    if index == n:
        if sum == total-sum:
            print("YES")
            sys.exit(0)  # 프로그램을 끝내버리기
    else:
        DFS(index+1, sum+col[index])
        DFS(index+1, sum)


if __name__ == "__main__":
    n = int(input())
    col = list(map(int, input().split()))
    total = sum(col)
    DFS(0, 0)
    print("NO")

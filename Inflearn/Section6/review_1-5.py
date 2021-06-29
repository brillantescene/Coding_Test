# 1. 재귀함수를 이용한 이진수 출력
'''
def get_binary(n):
    if n == 0:
        # print(n, end='')
        return
    else:
        get_binary(n//2)
        print(n % 2, end='')


if __name__ == "__main__":
    get_binary(int(input()))
'''

# 2. 이진트리 순회 (깊이 우선 탐색)
'''
def binary_traversal(n):
    if n > 7:
        return
    else:
        # print(n, end=" ") 전위
        binary_traversal(2*n)
        # print(n, end=" ") 중위
        binary_traversal(2*n+1)
        # print(n, end=" ") 후위


if __name__ == "__main__":
    binary_traversal(1)
'''

# 부분집합 구하기 (DFS)

'''
def get_subset(n, level, ch):
    if level == n+1:
        tmp = []
        for i in range(1, n+1):
            if ch[i] == 1:
                tmp += [i]
        return [tmp]
    else:
        ans = []
        ch[level] = 1
        ans += get_subset(n, level+1, ch)
        ch[level] = 0
        ans += get_subset(n, level+1, ch)
    return ans


def solution(n):
    ch = [0] * (n+1)
    return get_subset(n, 0, ch)

print(solution(3))
'''

'''
def get_subset(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i]:
                print(i, end=" ")
        print()
    else:
        check[v] = 1
        get_subset(v+1)
        check[v] = 0
        get_subset(v+1)


if __name__ == "__main__":
    n = int(input())
    check = [0]*(n+1)
    get_subset(1)
'''

# 합이 같은 부분집합 DFS - 아마존 인터뷰

'''
def dfs(n, num, idx, sum, total):
    if sum > total // 2:
        return 0
    if idx == n:
        if sum == total-sum:
            return 1
        return 0
    else:
        ans = 0
        ans += dfs(n, num, idx+1, sum, total)
        ans += dfs(n, num, idx+1, sum+num[idx], total)
    return ans


def solution(n, num):
    return "YES" if dfs(n, num, 0, 0, sum(num)) else "NO"


print(solution(9, [3, 6, 13, 11, 7, 16, 34, 23, 12]))
'''

'''
def dfs(idx, sum):
    if sum > total//2:  # cut-edge
        return
    if idx == n:
        if sum == total-sum:
            print("YES")
            exit(0)
    else:
        dfs(idx+1, sum)
        dfs(idx+1, sum+arr[idx])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    dfs(0, 0)
    print("NO")
'''

# 바둑이 승차 DFS


def dfs(c, n, weight, idx, sum):
    if sum > c:
        return 0
    if idx == n:
        return sum
    else:
        ans = 0
        ans = max(dfs(c, n, weight, idx+1, sum),
                  dfs(c, n, weight, idx+1, sum+weight[idx]))
    return ans


def solution(c, n, weight):
    return dfs(c, n, sorted(weight), 0, 0)


print(solution(259, 5, [81, 58, 42, 33, 61]))


'''
def dfs(idx, sum, tsum):
    global max_weight
    if sum + (total - tsum) < max_weight:
        return
    if sum > c:
        return
    if idx == n:
        if max_weight < sum:
            max_weight = sum
        return
    else:
        dfs(idx+1, sum, tsum+weight[idx])
        dfs(idx+1, sum+weight[idx], tsum+weight[idx])


if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    total = sum(weight)
    max_weight = 0
    dfs(0, 0, 0)
    print(max_weight)
'''

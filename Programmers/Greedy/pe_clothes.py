def solution(n, lost, reserve):
    answer = 0
    l = [1]*(n+1)
    for i in lost:
        l[i] -= 1
    for i in reserve:
        l[i] += 1
    print(l)
    for i in range(1, n+1):
        if l[i] == 2:
            if i < n and l[i+1] == 0:
                l[i+1] = 1
                l[i] -= 1
            elif l[i-1] == 0 and l[i] == 2:
                l[i-1] = 1
                l[i] -= 1
    for x in l[1:]:
        if x >= 1:
            answer += 1
    print(l)
    return answer


print(solution(5, [2, 4], [2]))

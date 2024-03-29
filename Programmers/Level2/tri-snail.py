def solution(n):
    answer = []
    res = [[0]*n for _ in range(n)]

    num = 1
    x, y = -1, 0
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1
    for r in res:
        for x in r:
            if x:
                answer.append(x)
    return answer


print(solution(4))

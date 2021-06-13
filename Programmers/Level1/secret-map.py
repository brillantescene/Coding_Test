# 2018 카카오 공채 1차
# 비밀지도

def to_binary(n, num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    while len(binary) < n:
        binary = '0'+binary
    return binary


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = to_binary(n, arr1[i])
        arr2[i] = to_binary(n, arr2[i])

    print(int(arr1[0][0]) | int(arr2[0][0]))
    for i in range(n):
        tmp = ''
        for j in range(n):
            if int(arr1[i][j]) | int(arr2[i][j]) == 1:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

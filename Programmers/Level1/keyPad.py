# 2020 카카오 인턴십
# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    result = ''
    left = 10
    right = 12
    # keyPad = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9],
    #           ['*', 0, '#']]
    keyPad = {}
    x = 1
    keyPad[0] = (3, 1)
    for i in range(3):
        for j in range(3):
            keyPad[x] = (i, j)
            x += 1
    keyPad[x] = (3, 0)
    keyPad[x+2] = (3, 2)
    print(keyPad)

    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left = num
        elif num in [3, 6, 9]:
            result += 'R'
            right = num
        else:
            left_sub = abs(keyPad[num][0]-keyPad[left][0]) + \
                abs(keyPad[num][1]-keyPad[left][1])
            right_sub = abs(keyPad[num][0]-keyPad[right][0]) + \
                abs(keyPad[num][1]-keyPad[right][1])
            print(num, left_sub, right_sub)
            if left_sub < right_sub:
                result += 'L'
                left = num
            elif left_sub > right_sub:
                result += 'R'
                right = num
            else:
                if hand == 'right':
                    result += 'R'
                    right = num
                else:
                    result += 'L'
                    left = num
    return result


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([2, 5, 8, 0], "right"))

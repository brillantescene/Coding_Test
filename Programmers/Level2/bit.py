# 월간 코드 챌린지 시즌 2
# 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:

        if number % 2 == 0:
            answer.append(number+1)
        else:
            number = bin(number)[2:]
            number = number.zfill(len(number)+1)
            for i in range(len(number)-1, -1, -1):
                if number[i] == '0':
                    number = number[:i] + number[i+1] + \
                        number[i] + number[i+2:]

                    answer.append(int(number, 2))
                    print(int(number, 2))
                    break

    return answer


'''
시간 초과
def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = bin(number)[2:]
        next_num = number
        while True:
            next_num += 1
            tmp = bin(next_num)[2:]
            length = len(bin_number) if len(
                bin_number) > len(tmp) else len(tmp)
            tmp = tmp.zfill(length)
            bin_number = bin_number.zfill(length)
            cnt = 0
            for i in range(length):
                if abs(int(tmp[i])-int(bin_number[i])) == 1:
                    cnt += 1
            if cnt <= 2:
                answer.append(next_num)
                break
    return answer
'''

print(solution([2, 7]))

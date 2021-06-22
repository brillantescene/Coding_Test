# 월간 코드 챌린지 시즌 1
# 두 개 뽑아서 더하기

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        print(f"i {i}")
        for j in range(i+1, len(numbers)):
            print(numbers[i]+numbers[j])
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    return sorted(answer)


print(solution([5, 0, 2, 7]))
# print(solution([2, 1]))

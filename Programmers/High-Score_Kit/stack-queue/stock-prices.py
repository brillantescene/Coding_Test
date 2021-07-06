def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                print(j-i)
                answer.append(j-i)
                break
        else:
            print(j-i)
            answer.append(j-i)

    return answer

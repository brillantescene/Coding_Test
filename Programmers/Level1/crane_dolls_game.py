# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        for i in range(len(board)):
            tmp = board[i][move]
            if tmp != 0:
                if bucket and tmp == bucket[-1]:
                    answer += 2
                    bucket.pop()
                else:
                    bucket.append(tmp)
                board[i][move] = 0
                break
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))

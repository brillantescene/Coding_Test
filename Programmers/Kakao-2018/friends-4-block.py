# level2 프렌즈4블록

def solution(m, n, board):
    answer = 0
    check = True
    board = [list(x) for x in board]

    while check:

        check = []

        # 4블럭 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j] != '#':
                    check.append((i, j))

        for i, j in check:
            board[i][j] = board[i][j + 1] = '#'
            board[i + 1][j + 1] = board[i + 1][j] = '#'

        for _ in range(m):
            for i in range(1, m):
                for j in range(n):
                    if board[i][j] == '#':
                        board[i][j], board[i-1][j] = board[i-1][j], '#'
    # print(*board)
    return sum(b.count('#') for b in board)


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))


# b = list(map(list, zip(*board)))
#     # print(b)
#     print(*board)
#     print(list(zip(*board)))
#     print(board[0][3])

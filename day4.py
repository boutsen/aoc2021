f = open("inputs/day4", "r")


def create_board(input):
    board = {}
    for i, line in enumerate(input.split("\n")):
        for j, num in enumerate(line.split()):
            board[(i, j)] = int(num)
    return board


DRAWS = [int(draw) for draw in f.readline().split(",")]
BOARDS = [create_board(board.strip()) for board in f.read().split("\n\n")]


def mark_num(board, num):
    index = [(x, y) for x, y in board if board[(x, y)] == num]
    if index:
        board[index[0]] = -board[index[0]]
    return board


def bingo(board):
    for c in range(0, 5):
        if all(num < 0 for num in [board[(x, y)] for x, y in {(c, 0), (c, 1), (c, 2), (c, 3), (c, 4)}]):
            return True
        if all(num < 0 for num in [board[(y, x)] for x, y in {(c, 0), (c, 1), (c, 2), (c, 3), (c, 4)}]):
            return True
    return False


def play_bingo(draws, boards):
    count = 0
    nr_of_boards = len(boards)
    for draw in draws:
        boards = [mark_num(board, draw) for board in boards]
        if count > 5:
            for board in boards:
                if bingo(board):
                    # First BINGO
                    if len(boards) == nr_of_boards:
                        print("Part1:" + str(sum(board[(x, y)] for x, y in board if board[(x, y)] > 0) * draw))
                    # Last BINGO to finish
                    if len(boards) == 1:
                        print("Part2:" + str(sum(board[(x, y)] for x, y in board if board[(x, y)] > 0) * draw))
                        return
                    boards.remove(board)
        count += 1


play_bingo(DRAWS, BOARDS)

import re

f = open("inputs/day4", "r")


def create_board(input):
    board = []
    for line in input.split("\n"):
        board.extend(int(x) for x in line.split())
    return board

DRAWS = [int(draw) for draw in f.readline().split(",")]
BOARDS = [create_board(board) for board in f.read().split("\n\n")]


def mark_num(board,num):
    if num in board:
        board[board.index(num)] = -1
    return board


def bingo(board):
    for row in range(0,len(board)-5,5):
        if sum(board[row:row+5]) == -5:
            return True
    for col in range(0,5):
        if sum([board[col+i] for i in range(0,len(board),5)]) == -5:
            return True

    return False
    

def play_bingo(draws,boards):
    count = 0
    nr_of_boards = len(boards)
    for draw in draws:
        boards = [mark_num(board,draw) for board in boards]
        if count > 5:
            for board in boards:
                if bingo(board) and (len(boards) == nr_of_boards or len(boards) == 1):
                    return sum(unmarked for unmarked in board if unmarked > 0) * draw
        count += 1


print(play_bingo(DRAWS,BOARDS))
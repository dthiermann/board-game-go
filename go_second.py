import re

length = 5

example_board = [[ ['empty', '0'] for x in range(length)] for y in range(length)]


def print_board(board):
    for y in range(len(board)):
        row = ''
        for x in range(len(board)):
            row = row + board[x][y][0] + ' '

        print(row)
        
def print_everything(board):
    for y in range(len(board)):
        row = ''
        for x in range(len(board)):
            row = row + board[x][y][0] + ' '+ board[x][y][1] + ' '

        print(row)
    
def make_move(color, board, x, y, n):
    if board[x][y][0] != 'empty':
        print('error: point occupied')
    else:
        board[x][y] = [color,str(n)]
        
        

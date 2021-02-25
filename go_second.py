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
            row = row + board[x][y][0] + ' '+ str(board[x][y][1]) + ' '

        print(row)
    
def make_move(color, board, x, y, n):
    if board[x][y][0] != 'empty':
        print('error: point occupied')
    else:
        board[x][y] = [color, n]


def adjacent(x,y,board):
    
    nearby = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]

    neighbors = []
    
    for point in nearby:
        x_valid = point[0] in range(0, len(board))
        y_valid = point[1] in range(0, len(board))
        if x_valid and y_valid:
            neighbors.append(point)

    return neighbors


        

    

    

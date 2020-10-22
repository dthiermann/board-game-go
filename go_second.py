import re

length = 5

example_board = [[0 for x in range(length)] for y in range(length)]

example_board[2][1] = 3

def print_board(board):
    for y in range(len(board)):
        row = ''
        for x in range(len(board)):
            row = row + str(board[x][y])+' '

        print(row)

def adjacent(x,y,board):
    neighbors = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]

    real_neighbors = []

    for point in neighbors:
        if point[0] < 0 or point[0] >= len(board):
            pass
        elif point[1] < 0 or point[1] >= len(board):
            pass
        else:
            real_neighbors.append(point)

    return real_neighbors
                
            
    

    for point in neighbors:
        for coord in point:
            if coord < 0 or coord >= len(board):
                neighbors.remove(point)

    return neighbors

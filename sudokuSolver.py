#!/usr/bin/python3

from copy import deepcopy # used for copy board (lists) in bfs algorithm
from sys import argv # used for get filename passed as argument
import time # used for estimated time log

# Print board with normal 9x9 sudoku style
def printRealBoard(board):
    print('---------------------')
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(board[0])):
            if (j % 3 == 0 and j != 0):
                print(' | ', end = '')
            if (j == 8):
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ',end = '')
    print('---------------------')

# Print line board like input but with solved (I hope)
def printLineBoard(board):
    result = ''
    for i in range(9):
        for j in range(9):
            if (board[i][j] == 0):
                result += '.'
            else:
                result += str(board[i][j])

    print(result)

# Function used to find the first empty cell on board starting from top left corner to right columns and down rows
def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j] == 0):
                return (i, j)
    return None

# Function used to verify if the tested number is valid following sudoku line, columns and quadrants rules
def valid(board, num, pos):
    # check line
    for i in range(9):
        if (board[pos[0]][i] == num and pos[1] != i):
            return False

    # check column
    for j in range(9):
        if (board[j][pos[1]] == num and pos[0] != j):
            return False

    # check quadrant
    quad_x = pos[1] // 3 #used integer division to get the integer value from positions
    quad_y = pos[0] // 3
    for i in range(quad_y * 3, quad_y * 3 + 3):
        for j in range(quad_x * 3, quad_x * 3 + 3):
            if (board[i][j] == num and (i, j) != pos):
                return False
    return True

# Function for BFS solution
def solveBFS(board):
    # search for the first empty cell
    find = findEmpty(board)

    if (not find):
        # if not have empty cells, then the sudoku is solved
        printLineBoard(board)
        return True
    else:
        # if have a empty cell, get the row and column index
        row, col = find

    # create a array of possible board solutions
    solutions = []

    # loop to test all possible values 1 to 9
    for i in range(1,10):
        # verify if is a valid number, considering sudoku rules
        if (valid(board, i , (row,col))):
            # copy the actual board to a new one
            newList = deepcopy(board)

            # insert the new valid value to the new board
            newList[row][col] = i

            # append board to the list
            solutions.append(newList)

    # loop to test all possibilities for the last validation
    for i in range(len(solutions)):
        # call recursive solveBFS to continue the actual solution board
        # if the result is true, the sudoku has been solved
        # if not, continue to next possible board
        if (solveBFS(solutions[i])):
            return True

    return False

# Function for DFS solution
def solveDFS(board):
    # search for the first empty cell
    find = findEmpty(board)

    if not find:
        # if not have empty cells, then the sudoku is solved
        printLineBoard(board)
        return True
    else:
        # if have a empty cell, get the row and column index
        row, col = find

    # loop to test all possible values 1 to 9
    for i in range(1,10):
        # verify if is a valid number, considering sudoku rules
        if (valid(board, i , (row,col))):
            # insert the valid value to board
            board[row][col] = i

            # call solveDFS recursive to continue this board
            # if the result is true, the sudoku has been solved
            if (solveDFS(board)):
                return True
            # if not, change the actual valid value to 0 and continue testing next value
            board[row][col] = 0

    return False

# Function for AStar solution
def solveAStar(board):
    # create a array of possible board solutions
    solutions = []

    # loop to run in all board
    for i in range(9):
        for j in range(9):
            # create a list with all posibilities
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            # check if cell is empty
            if (board[i][j] == 0):
                # loop to verify and remove incorrect numbers from row, column and quadrant
                for k in range(9):
                    if (board[i][k] != 0 and board[i][k] in x):
                        x.remove(board[i][k])
                    if (board[k][j] != 0 and board[k][j] in x):
                        x.remove(board[k][j])
                quad_x = j // 3 #used integer division to get the integer value from positions
                quad_y = i // 3
                for m in range(quad_y * 3, quad_y * 3 + 3):
                    for n in range(quad_x * 3, quad_x * 3 + 3):
                        if (board[m][n] != 0 and board[m][n] in x and (m, n) != (i,j)):
                            x.remove(board[m][n])
                tmp = []
                tmp.append(i)
                tmp.append(j)
                tmp.append(len(x))
                tmp.append(x)

                # insert ordered, lowest first
                index = 0
                for k in range(len(solutions)):
                    if (solutions[k][2] > tmp[2] and tmp[2] > 0):
                        index = k
                        break
                    else:
                        index+=1
                solutions.insert(index, tmp)

    if (len(solutions) > 0):
        row = solutions[0][0]
        col = solutions[0][1]

        # loop in array of solutions of current recursion
        for i in solutions[0][3]:
            # insert the valid value to board
            board[row][col] = i

            # if not find empty cell print result or call recursive to next cell
            if (not findEmpty(board)):
                printLineBoard(board)
                return True
            elif solveAStar(board):
                return True
            # if not, change the actual valid value to 0 and continue testing next value
            board[row][col] = 0

        return False

# if user use command sudokuSolver.py bfs|dfs|astar < input.txt
# this case is necessary read the input text
if (len(argv) == 2):
    if (argv[1].lower() != 'bfs' and argv[1].lower() != 'dfs' and argv[1].lower() != 'astar'):
        print('Please use following command:\n\nsudokuSolver.py bfs|dfs|astar input.txt \nor\nsudokuSolver.py bfs|dfs|astar < input.txt\n')
    else:
        while True:
            try:
                board = []
                inputLine = input()
                for i in range(9):
                    line = []
                    for j in range (9):
                        if (inputLine[j+(i*9)] == '.'):
                            line.append(0)
                        else:
                            line.append(int(inputLine[j+(i*9)]))
                    board.append(line)

                # for log time elapsed just uncomment line 293, 306 and 307
                # startTime = time.time()
                if (argv[1].lower() == 'bfs'):
                    solveBFS(board)
                elif (argv[1].lower() == 'dfs'):
                    solveDFS(board)
                elif (argv[1].lower() == 'astar'):
                    solveAStar(board)

                #elapsedTime = time.time() - startTime
                #print("Elapsed time(s): " + str(elapsedTime))
            except Exception as e:
                break

# if user use command sudokuSolver.py bfs|dfs|astar input.txt
# this case is necessary open the passed filename line by line
elif (len(argv) == 3):
    if (argv[1].lower() != 'bfs' and argv[1].lower() != 'dfs' and argv[1].lower() != 'astar'):
        print('Please use following command:\n\nsudokuSolver.py bfs|dfs|astar input.txt \nor\nsudokuSolver.py bfs|dfs|astar < input.txt\n')
    else:
        inputFile = open(argv[2])
        while True:
            try:
                board = []
                inputLine = inputFile.readline()
                for i in range(9):
                    line = []
                    for j in range (9):
                        if inputLine[j+(i*9)] == '.':
                            line.append(0)
                        else:
                            line.append(int(inputLine[j+(i*9)]))
                    board.append(line)

                # for log time elapsed just uncomment line 332, 345 and 346
                #startTime = time.time() #uncomment for log time
                if (argv[1].lower() == 'bfs'):
                    solveBFS(board)
                elif (argv[1].lower() == 'dfs'):
                    solveDFS(board)
                elif (argv[1].lower() == 'astar'):
                    solveAStar(board)

                #elapsedTime = time.time() - startTime  #uncomment for log time
                #print("Elapsed time(s): " + str(elapsedTime))  #uncomment for log time
            except Exception as e:
                inputFile.close()
                break
else:
    print('Please use following command:\n\nsudokuSolver.py bfs|dfs|astar input.txt \nor\nsudokuSolver.py bfs|dfs|astar < input.txt\n')
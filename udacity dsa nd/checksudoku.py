"""
In the next exercise, you will write a function that checks sudoku squares for correctness.

Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. 
For this question we will generalize and simplify the game.

Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:

Each column of the square contains each of the whole numbers from 1 to n exactly once.

Each row of the square contains each of the whole numbers from 1 to n exactly once.

You may assume that the input is square and contains at least one row and column.
"""
#this program has important an important logic of checking for element if occurring more than once

#.. using check_list and checking element in it if it's not here then return False if here then remove it
#this logic can be modified accordingly as now it is as per the sudoku check(slight changes are required for particular application
# because here we are making check_list for valid values in square of sudoku(eg. 1 to 4 for a 4x4 square and 1 to 9 for 9x9 square and so
#on .. Here the checklist is initially a list of elements that are expected in the sudoku   
# values other than 1 to 9 are invalid
# values other than 1 to n (for nxn sudoku) are invalid    eg. 'a' ,'b' ,'c'....... are invalid for sudoku



eg_sudoku = [                                                     # 4x4 square
    [1,2,3,4],
    [2,3,1,4],
    [4,1,2,3],
    [3,4,1,2]
]

eg_sudoku2 = [
    [1,2,4,3],
    [2,4,3,1],
    [3,1,2,4],
    [4,3,1,2]
]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]



def check_sudoku(square):
    #checking the rows
    for row in square:
        check_list = list(range(1, len(square)+1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    

    #checking the columns
    for n in range(len(square)):
        check_list = list(range(1, len(square)+1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    
    return True                                    #true if no duplicacy and invalidity in elements found



print(check_sudoku(eg_sudoku))         #False
print(check_sudoku(eg_sudoku2))         #True

print(check_sudoku(incorrect4))         #False







#more examples for testing
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]


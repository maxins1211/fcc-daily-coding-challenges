# Matrix Shift
# Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.

# A positive shift moves values to the right.
# A negative shift moves values to the left.
# Values should wrap:

# Treat the matrix as one continuous sequence of values.
# When a value moves past the end of a row, it continues at the beginning of the next row.
# When a value moves past the last position in the matrix, it wraps to the first position.
# The same applies in reverse when shifting left.
# For example, given:

# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]

# with a shift of 1, move all the numbers to the right one:

# [
#   [6, 1, 2],
#   [3, 4, 5]
# ]
# [
#   [5,6,1],
#   [2,3,4]
# ]
from typing import List
def shift_matrix(matrix: List[List[int]], shift:int) -> List[List[int]]:
    row:int=len(matrix)
    column:int = len(matrix[0])
    flatted_matrix: List[int] = flat_matrix(matrix)
    temp_arr: List[int] = shift_right(flatted_matrix,shift)
    return build_matrix(temp_arr,row,column)

def flat_matrix(matrix: List[List[int]]) -> List[int]:
    arr: List[int] = []
    for row in range (0,len(matrix)):
        for column in range(0,len(matrix[row])):
            arr.append(matrix[row][column])
    return arr

def shift_right(matrix:List[int], shift:int) -> List[int]:
    arr: List[int] = []
    shift = shift % (len(matrix))
    if(shift < 0):
        shift = shift * (len(matrix)-1) * (-1)
    for  i in range(0,shift):
        poppedElement: int = matrix.pop()
        arr.append(poppedElement)
    arr.reverse()
    for i in range(0,len(matrix)):
        arr.append(matrix[i])
    return arr

def build_matrix(arr: List[int],row:int,column:int) -> List[List[int]]:
    matrix: List[List[int]] =[[0 for _ in range(column)] for _ in range(row)]
    for i in range(0,row):
        for j in range(0,column):
            matrix[i][j]=arr[i*column+j]
    return matrix
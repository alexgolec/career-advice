# https://leetcode.com/problems/unique-paths


def unique_paths(rows, cols):
    # Initialize an empty matrix
    matrix = [(lambda: [(lambda: 0)() for i in range(cols)])()
            for j in range(rows)]

    # Initialize the top row and leftmost column with 1's
    for col in range(cols):
        matrix[0][col] = 1
    for row in range(rows):
        matrix[row][0] = 1

    # The recurrence relation: Each element of the matrix except for the top row 
    # and the leftmost column is equal to the sum of the entry above and to the 
    # left of it.
    for row in range(1, rows):
        for col in range(1, cols):
            matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]

    return matrix[-1][-1]


def memory_efficient_unique_paths(rows, cols):
    '''
    Strictly speaking, we don't actually need the entire matrix, only the
    previous row. We can reduce the memory footprint by reusing a single row 
    object.
    '''
    # Initialize an empty matrix
    current_row = [0 for i in range(cols)]
    last_row = [1 for i in range(cols)]

    # The recurrence relation: Each element of the matrix except for the top row 
    # and the leftmost column is equal to the sum of the entry above and to the 
    # left of it.
    for row in range(1, rows):
        current_row[0] = 1
        for col in range(1, cols):
            current_row[col] = current_row[col - 1] + last_row[col]

        current_row, last_row = last_row, current_row

    return last_row[-1]


class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        return memory_efficient_unique_paths(rows, cols)

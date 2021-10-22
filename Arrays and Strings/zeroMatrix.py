'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''

def zeroMatrix(matrix):

    rows, cols = len(matrix), len(matrix[0])
    zeroRows, zeroCols = [], []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRows.append(i)
                zeroCols.append(j)

    for i in zeroRows:
        for j in range(cols):
            matrix[i][j] = 0

    for j in zeroCols:
        for i in range(rows):
            matrix[i][j] = 0

    return matrix

matrix = [[1,1,0],[1,1,1],[1,1,1]]
print(zeroMatrix(matrix))
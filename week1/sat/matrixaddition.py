matrix = [[1, 3, 2],
         [2, 4, 4]]
matrix2 = [[5, 2, 2],
          [1, 0, 4]]
matrix3 = [[0, 0, 0],
          [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix3[i][j] = (matrix[i][j] + matrix2[i][j])
for i in matrix3:
    print(i)
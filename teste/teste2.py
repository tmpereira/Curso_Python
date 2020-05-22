'''
matrix =[[1,2,3],[4,5,6],[3,6,7]]
matrix3x = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matrix3x[i][j] = 3*matrix[i][j]
        print(str(matrix3x[i][j]) + ' ',end='')
    print('')
'''

import numpy as np

m =[[1,2,3],[4,5,6],[3,6,7]]
mndarray = np.array(m)
m[0,0]
m[0][0]


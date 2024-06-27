def isToeplitz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>0 and j>0 and mat[i][j] != mat[i-1][j-1]:
                return False
            if i<len(mat)-1 and j<len(mat[0])-1 and mat[i][j] != mat[i+1][j+1]:
                return False
    return True 
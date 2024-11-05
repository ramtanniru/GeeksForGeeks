def transpose(mat):
    temp = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            temp[i][j] = mat[j][i]
    return temp
    
def rotate(mat): 
    temp = transpose(mat)
    for i in range(len(temp)):
        for j in range(len(temp)):
            mat[i][j] = temp[i][len(temp)-j-1]
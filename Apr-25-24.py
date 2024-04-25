class Solution:
    def findMaxSum(self,n,m,mat):
        maxSum = 0
        if n<3 or m<3:
            return -1
        for i in range(len(mat)-2):
            for j in range(len(mat[0])-2):
                s = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
                maxSum = max(s,maxSum)
        return maxSum
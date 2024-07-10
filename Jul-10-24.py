class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        dp = [[0]*len(mat[0]) for i in range(len(mat))]
        maxArea = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    maxArea = max(maxArea,dp[i][j])
        return maxArea 
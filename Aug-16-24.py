class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        choice = [x,y,z]
        dp = [float('-inf') for i in range(n+1)]
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in choice:
                if j<=i:
                    dp[i] = max(dp[i],dp[i-j]+1)
        if dp[-1]==float('-inf'):
            return 0
        return dp[-1] 
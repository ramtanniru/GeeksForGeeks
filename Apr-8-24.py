class Solution:
    def optimalStrategyOfGame(self,n, arr):
        dp = [[-1]*n for i in range(n)]
        def solve(arr,l,r,dp):
            if l>r :
                return 0
            if l==r:
                return arr[l]
            if dp[l][r] != -1 :
                return dp[l][r]
            left = arr[l] + min(solve(arr,l+2,r,dp),solve(arr,l+1,r-1,dp))
            right = arr[r] + min(solve(arr,l+1,r-1,dp),solve(arr,l,r-2,dp))
            dp[l][r] = max(left,right)
            return dp[l][r]
        return solve(arr,0,n-1,dp)
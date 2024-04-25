class Solution:
    def __init__(self):
        self.dp = dict()
    # DP using Backtracking but giving TLE 433/1115 passed
    def ways(self, n,m):
        def bt(n,m):
            if n==0 or m==0:
                return 1
            if (n,m) in self.dp:
                return self.dp[(n,m)]
            self.dp[(n,m)] = (bt(n-1,m) + bt(n,m-1))%1000000007
            return self.dp[(n,m)]
        return bt(n,m)
    # DP using tabulation
    def ways(self, n,m):
        dp = [[0]*(m+1) for i in range(n+1)]
        # base case
        # when x=0 or y=0 we have only one way
        for i in range(m+1):
            dp[0][i] = 1
        for i in range(n+1):
            dp[i][0] = 1
        # filling the 2D DP array
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
        return dp[n][m]

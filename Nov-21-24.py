class Solution:
    def maximumProfit(self, prices) -> int:
        def rec(i=0,canBuy=1):
            if i==len(prices):
                return 0
            if dp[i][canBuy]!=-1:
                return dp[i][canBuy]
            if canBuy:
                pick = - prices[i] + rec(i+1,0)
                notPick = rec(i+1,1)
            else:
                pick = prices[i] + rec(i+1,1)
                notPick = rec(i+1,0)
            dp[i][canBuy] = max(pick,notPick)
            return dp[i][canBuy]
        dp = [[-1,-1] for i in range(len(prices))]
        return rec()
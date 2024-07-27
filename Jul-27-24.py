class Solution:
    def countMin(self, s):
        if s==s[::-1]:
            return 0
        dp = [[0]*(len(s)+1) for i in range(len(s)+1)]
        # longest palindormic subsequence
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==s[::-1][j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return len(s)-dp[len(s)][len(s)] 
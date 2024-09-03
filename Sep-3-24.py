class Solution:
	def minOperations(self, str1, str2):
		dp = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
		for i in range(1,len(dp)):
		    for j in range(1,len(dp[0])):
		        if str1[i-1]==str2[j-1]:
		            dp[i][j] = 1 + dp[i-1][j-1]
		        else:
		            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	    return len(str1)+len(str2)-2*dp[-1][-1] 
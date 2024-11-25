class Solution:
	def maxProduct(self,arr):
		pre,suf = 1,1
		res = float('-inf')
		n = len(arr)
		for i in range(n):
		    if pre==0: pre = 1
		    if suf==0: suf = 1
		    pre *= arr[i]
		    suf *= arr[n-i-1]
		    res = max(res,suf,pre)
		return res
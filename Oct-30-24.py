from collections import defaultdict
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	s = defaultdict(int)
    	ans = 0
    	for i in arr:
    	    if i+k in s:
    	        ans += s[i+k]
    	    if i-k in s:
    	        ans += s[i-k]
    	    s[i] += 1
    	return ans
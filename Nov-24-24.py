class Solution:
    def maxSubArraySum(self,arr):
        s = 0
        ans = float('-inf')
        for i in arr:
            s += i
            ans = max(ans,s)
            if s<0:
                s = 0
        return ans
class Solution:
    def maxSubArraySum(self,arr):
        s = 0
        res = float('-inf')
        for i in arr:
            s += i
            res = max(res,s)
            if s<0:
                s = 0
        return res 
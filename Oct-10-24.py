class Solution:
    def maxDistance(self, arr):
        m = dict()
        ans = 0
        for i,x in enumerate(arr):
            if x not in m:
                m[x] = i
            else:
                ans = max(ans,i-m[x])
        return ans 
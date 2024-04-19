class Solution:
    def findMissing(self,a,b,n,m):
        s = set(b)
        ans = []
        for i in a:
            if i not in s:
                ans.append(i)
        return ans
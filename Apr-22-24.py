class Solution:
    def minRow(self,n,m,a):
        d = {}
        for i in range(len(a)):
            d[i] = sum(a[i])
        m = [0,d[0]]
        for i in range(len(a)):
            if d[i]<m[1]:
                m = [i,d[i]]
        return m[0]+1
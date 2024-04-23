class Solution:
    def firstElement (self, n):
        l = [0,1]
        for i in range(n-1):
            l.append((l[i]+l[i+1])%1000000007)
        return l[-1]
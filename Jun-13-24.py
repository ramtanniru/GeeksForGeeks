class Solution:
    def padovanSequence(self, n):
        a,b,c,res = 1,1,1,2
        mod = 10**9 + 7
        if n<=2:
            return 1
        for i in range(3,n+1):
            res = (a+b)%mod
            a = b
            b = c
            c = res
        return res
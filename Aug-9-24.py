class Solution:
    def Maximize(self, a): 
        mod = 10**9 + 7
        a.sort()
        s = 0
        for i,x in enumerate(a):
            s += i*x % mod
        return s % mod 
    
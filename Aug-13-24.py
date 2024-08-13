class Solution:
    def floorSqrt(self, n): 
        i = 1
        while i*i<=n:
            if i*i==n:
                return i
            i += 1
        return i-1 
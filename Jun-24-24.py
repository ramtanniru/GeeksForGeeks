class Solution:
    def sumMatrix(self, n, q):
        if q==1 or q>2*n:
            return 0
        if q<=n+1:
            return q-1
        else:
            return 2*n - q + 1 
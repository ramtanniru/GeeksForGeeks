class Solution:
    def missingNumber(self, n, arr):
        t = (n*(n+1))//2
        return t-sum(arr) 
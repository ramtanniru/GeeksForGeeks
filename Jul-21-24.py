class Solution:
    def findMaxProduct(self, arr):
        if len(arr)==1:
            return arr[0]
        cntNeg = 0
        cntZero = 0
        maxNeg = float('-inf')
        prod = 1
        mod = (10**9)+7
        for i in arr:
            if i==0:
                cntZero += 1
                continue
            elif i<0:
                cntNeg += 1
                maxNeg = max(maxNeg,i)
            prod *= i
        if cntZero==len(arr):
            return 0
        if cntNeg&1:
            if cntNeg==1 and cntZero>0 and cntZero+cntNeg==len(arr):
                return 0
            prod = prod//maxNeg
        return prod%mod 
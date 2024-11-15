class Solution:
    def getSecondLargest(self, arr):
        a,b = -1,-1
        for i in arr:
            if i>a:
                b = a
                a = i
            elif i>b and i!=a:
                b = i
        return b
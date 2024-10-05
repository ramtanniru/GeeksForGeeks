class Solution:
    def findSmallest(self, arr):
        s = 1
        for i in arr:
            if i>s:
                return s
            s += i
        return s
class Solution:
    def findExtra(self,n,a,b):
        i = 0
        while i<min(len(a),len(b)):
            if a[i]!=b[i]:
                return i
            i += 1
        return i
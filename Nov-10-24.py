class Solution:
    def findUnion(self,a,b):
        res = []
        i = 0 # a array pointer
        j = 0 # b array pointer
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i]<b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        while i<len(a):
            res.append(a[i])
            i += 1
        while j<len(b):
            res.append(b[j])
            j += 1
        return res
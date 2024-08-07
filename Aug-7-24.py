class Solution:
    def kthElement(self, k, arr1, arr2):
        def merge(a,b):
            res = []
            i,j = 0,0
            while i<len(a) and j<len(b):
                if a[i]<b[j]:
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
        return merge(arr1,arr2)[k-1] 
    
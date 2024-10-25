class Solution:
    def alternateSort(self,arr):
        arr.sort()
        i,j = 0,len(arr)-1
        res = []
        while i<j:
            res.append(arr[j])
            res.append(arr[i])
            i += 1
            j -= 1
        if i==j:
            res.append(arr[i])
        return res
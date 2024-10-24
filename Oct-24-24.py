class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        if len(arr)<2: return arr
        i,j = 0,1
        zeros = 0
        res = []
        while j<len(arr):
            if arr[i]==arr[j] and arr[i]!=0:
                arr[i] = arr[i]*2
                arr[j] = 0
            i += 1
            j += 1
        for i in arr:
            if i!=0:
                res.append(i)
            else:
                zeros += 1
        for i in range(zeros):
            res.append(0)
        return res
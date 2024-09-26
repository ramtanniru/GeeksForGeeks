class Solution:
    def maxStep(self, arr):
        if len(arr)==1: return 0
        maX = 0
        i,j = 0,1
        cnt = 0
        while j<len(arr):
            if arr[i]<arr[j]:
                cnt += 1
                maX = max(maX,cnt)
            else:
                cnt = 0
            i += 1
            j += 1
        return maX 
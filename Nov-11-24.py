class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        cnt = 0
        i,j = 0,1
        while j<len(arr):
            if arr[i]>=arr[j]:
                cnt += arr[i]-arr[j]+1
                arr[j] = arr[i]+1
            i += 1
            j += 1
        return cnt
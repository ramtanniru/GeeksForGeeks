class Solution:
    def pairWithMaxSum(self, arr):
        if len(arr)<2:
            return -1
        i,j = 0,1
        maX = 0
        while j<len(arr):
            maX = max(maX,arr[i]+arr[j])
            i += 1
            j += 1
        return maX
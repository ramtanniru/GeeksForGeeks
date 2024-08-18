class Solution:
    def canSplit(self, arr):
        lSum,rSum,l,r = 0,0,0,len(arr)-1
        while l<=r:
            if lSum<rSum:
                lSum += arr[l]
                l += 1
            else:
                rSum += arr[r]
                r -= 1
        return lSum==rSum 
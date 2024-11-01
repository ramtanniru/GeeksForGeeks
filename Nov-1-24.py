class Solution:
    def maxSum(self,arr):
        def solve(arr):
            ans = 0
            for i in range(len(arr)):
                ans += abs(arr[i]-arr[i-1])
            return ans
        arr.sort()
        n = len(arr)
        shuffledList = [0]*n
        i,j = 0,0
        while i<=n//2 and j<n:
            shuffledList[j] = arr[i]
            j += 2
            i += 1
        i,j = n-1,1
        while i>=0 and j<n:
            shuffledList[j] = arr[i]
            i -= 1
            j += 2
        return solve(shuffledList)
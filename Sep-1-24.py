class Solution:
    def maxPathSum(self, arr1, arr2):
        i,j = 0,0
        s1,s2 = 0,0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                s1 += arr1[i]
                i += 1
            elif arr1[i]>arr2[j]:
                s2 += arr2[j]
                j += 1
            else:
                temp = max(s1,s2)
                s1 = temp + arr1[i]
                s2 = temp + arr2[j]
                i += 1
                j += 1
        while i<len(arr1):
            s1 += arr1[i]
            i += 1
        while j<len(arr2):
            s2 += arr2[j]
            j += 1
        return max(s1,s2) 
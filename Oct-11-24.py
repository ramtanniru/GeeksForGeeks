class Solution:
    def rearrange(self, arr):
        s = set(arr)
        for i in range(len(arr)):
            if i in s:
                arr[i] = i
            else:
                arr[i] = -1
        return arr
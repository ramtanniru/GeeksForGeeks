class Solution:
    def rearrange(self,arr):
        pos = [i for i in arr if i>=0]
        neg = [i for i in arr if i<0]
        i = 0
        j = 0
        while i<len(pos) and i<len(neg):
            arr[j] = pos[i]
            j += 1
            arr[j] = neg[i]
            i += 1
            j += 1
        while i<len(pos):
            arr[j] = pos[i]
            j += 1
            i += 1
        while i<len(neg):
            arr[j] = neg[i]
            j += 1
            i += 1
        return arr 
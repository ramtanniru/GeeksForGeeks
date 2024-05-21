class Solution:
    def printKClosest(self, arr, n, k, x):
        s = set(arr)
        res = []
        i = 1
        while len(res)<k:
            if x+i in s:
                res.append(x+i)
            if x-i in s:
                res.append(x-i)
            i += 1
        return res[:k]
class Solution:
    def removeDuplicates(self, arr):
        s = set()
        res = []
        for i in arr:
            if i not in s:
                s.add(i)
                res.append(i)
        return res
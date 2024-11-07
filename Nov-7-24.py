class Solution:
    def findSplit(self, arr):
        total = sum(arr)
        if total%3!=0:
            return [-1,-1]
        target = int(total/3)
        i = 0
        cnt = 0
        res = []
        while i<len(arr):
            if cnt==target:
                res.append(i)
                cnt = 0
            if cnt>target:
                return [-1,-1]
            cnt += arr[i]
            i += 1
        return res[:2]
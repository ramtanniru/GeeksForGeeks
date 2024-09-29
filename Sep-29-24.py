class Solution:
    def totalCount(self, k, arr):
        cnt = 0
        for i in arr:
            cnt += i//k
            if i%k!=0:
                cnt += 1
        return cnt 
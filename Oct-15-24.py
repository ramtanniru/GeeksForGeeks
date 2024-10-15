from collections import defaultdict
class Solution:
    def subArraySum(self,arr, tar):
        pre = 0
        cache = defaultdict(int)
        cache[0] = 1
        cnt = 0
        for i in arr:
            pre += i
            if pre-tar in cache:
                cnt += cache[pre-tar]
            cache[pre] += 1
        return cnt
from collections import defaultdict
class Solution:
    def canAttend(self,arr):
        # sweepLine algorithm
        cache = defaultdict(int)
        for s,e in arr:
            cache[s] += 1
            cache[e] -= 1
        l = list(cache.keys())
        l.sort()
        rooms = 0
        for k in l:
            rooms += cache[k]
            if rooms>1:
                return False
        return True
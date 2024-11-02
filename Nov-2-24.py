class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        cache = defaultdict(int)
        for i,x in enumerate(arr):
            if x in cache:
                if i-cache[x]<=k: return True
            cache[x] = i
        return False
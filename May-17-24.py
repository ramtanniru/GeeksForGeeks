class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        k = set(arr)
        if x==0:
            d = dict(collections.Counter(arr))
            if max(d.values())>1:
                return 1
            else:
                return -1
        for i in arr:
            if x+i in k:
                return 1
        return -1
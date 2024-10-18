from collections import Counter
class Solution:
    def getSingle(self,arr):
        c = Counter(arr)
        for k,v in c.items():
            if v&1==1:
                return k
        return -1
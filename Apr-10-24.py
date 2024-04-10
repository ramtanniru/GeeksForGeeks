from collections import Counter
class Solution:
    def findSingle(self, n, arr):
        map = dict(Counter(arr))
        for i in map.keys():
            if map[i]%2!=0:
                return i
from collections import defaultdict,Counter
class Solution:
    def sortByFreq(self,arr):
        c = Counter(arr)
        d = defaultdict(list)
        for k,v in c.items():
            d[v].append(k)
        l = sorted(d.keys(),reverse=True)
        res = []
        for k in l:
            for v in sorted(d[k]):
                for i in range(k):
                    res.append(v)
        return res 
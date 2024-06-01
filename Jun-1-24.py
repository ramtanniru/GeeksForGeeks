import collections
class Solution:
    def oddEven(self, s : str) -> str:
        d = dict(collections.Counter(s))
        x,y = 0,0
        for i in d.keys():
            if ord(i)%2==0 and d[i]%2==0:
                y += 1
            if ord(i)%2!=0 and d[i]%2!=0:
                x += 1
        if (x+y)%2==0:
            return "EVEN"
        return "ODD"
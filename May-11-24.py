import math
class Solution:
    def jugglerSequence(self, n):
        res = [n]
        while res[-1]>1:
            if res[-1]%2==0:
                res.append(math.floor(res[-1]**0.5))
            else:
                res.append(math.floor(res[-1]**1.5))
        return res
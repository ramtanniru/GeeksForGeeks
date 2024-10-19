import sys
class Solution:
    def roundToNearest (self, s) : 
        def refactor(s):
            nonlocal preZeros
            return preZeros*"0"+str(s)
        sys.set_int_max_str_digits(100000)
        l = int(s)
        r = int(s)
        preZeros = 0
        for i in s:
            if i!='0':
                break
            preZeros += 1
        while l%10!=0 and r%10!=0:
            l -= 1
            r += 1
        if l%10==0 and r%10==0:
            return refactor(l)
        return refactor(l) if l%10==0 else refactor(r)
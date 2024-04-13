class Solution:
    def reversedBits(self, x):
        s = format(x,'b')
        v = ""
        for i in range(len(s),32):
            v+="0"
        s = v+s
        s = s[::-1]
        n = 0
        l = len(s)
        p = 31
        for i in s:
            if i=="1":
                n+=2**p
            p-=1
        return n
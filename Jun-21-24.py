class Solution:
    def compareFrac (self, str):
        a,b = str.split(", ")
        aNum,aDen = map(int,a.split("/"))
        bNum,bDen = map(int,b.split("/"))
        aVal = aNum/aDen
        bVal = bNum/bDen
        if aVal>bVal:
            return a
        elif aVal<bVal:
            return b
        else:
            return "equal"
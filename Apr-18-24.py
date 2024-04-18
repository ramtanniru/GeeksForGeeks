class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        s = set()
        l = []
        for i in arr:
            if i in s:
                l.append(i)
            else:
                s.add(i)
        return l
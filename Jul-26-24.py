from collections import Counter
class Solution:
    def kPangram(self,s, k):
        string = ""
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        li = [i for i in s if i in alpha]
        string = ''.join(li)
        if len(string)<26:
            return False
        d = Counter(string)
        return (26-len(d.keys()))<=k 
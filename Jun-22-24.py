class Solution:
    def ExtractNumber(self,sentence):
        l = sentence.split()
        num = []
        for i in l:
            try:
                if isinstance(int(i),int) and "9" not in i:
                    num.append(int(i))
            except:
                continue
        if not num:
            return -1
        return max(num) 
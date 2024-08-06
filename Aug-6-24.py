class Solution:
    def isValid(self, s):
        i = 0
        temp = ""
        cnt = 0
        while i<len(s):
            if s[i]==".":
                if not 0<len(temp)<=3 or not 0<=int(temp)<=255 or (len(temp)>1 and temp[0]=='0'):
                    return False
                cnt += 1
                temp = ""
                i += 1
                continue
            temp += s[i]
            i += 1
        if not 0<len(temp)<=3 or not 0<=int(temp)<=255 or (len(temp)>1 and temp[0]=='0'):
                    return False
        return cnt==3 
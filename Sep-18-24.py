class Solution:
    def ispar(self,x):
        open = '([{'
        stk = []
        map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in x:
            if i in open:
                stk.append(i)
            else:
                if not stk: return False
                if stk.pop()!=map[i]:
                    return False
        return True if not stk else False 
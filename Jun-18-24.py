class Solution:
    def rectanglesInCircle(self,r):
        cnt = 0
        d = (2*r)**2
        for i in range(1,2*r):
            for j in range(1,2*r):
                diaRect = i**2 + j**2
                if diaRect <= d:
                    cnt += 1
        return cnt
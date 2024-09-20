class Solution:
    def countBuildings(self, height):
        cnt,prev = 0,0
        for i in height:
            if i>prev:
                cnt += 1
                prev = i
        return cnt 
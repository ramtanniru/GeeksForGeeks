from typing import List
class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        def bt(i=0,j=0,path=""):
            nonlocal dir,res
            if not (0<=i<len(m) and 0<=j<len(m[0]) and m[i][j]==1):
                return
            if i==len(m)-1 and j==len(m[0])-1:
                res.append(path)
                return
            m[i][j] = 0
            for dx,dy,p in dir:
                x,y = i+dx,j+dy
                if 0<=x<len(m) and 0<=y<len(m[0]) and m[x][y]==1:
                    bt(x,y,path+p)
            m[i][j] = 1
            
        dir = [(0,1,'R'),(1,0,'D'),(0,-1,'L'),(-1,0,'U')]
        res = []
        bt()
        return res 
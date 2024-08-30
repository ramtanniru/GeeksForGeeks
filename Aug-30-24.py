class Solution:
    def nQueen(self, n):
        if n==0: return []
        def bt(row = 0):
            if row==n:
                res.append(l[:])
                return
            for i in range(n):
                if i in cols or row+i in diagonal or row-i in negDiagonal:
                    continue
                cols.add(i)
                diagonal.add(row+i)
                negDiagonal.add(row-i)
                l.append(i+1)
                bt(row+1)
                cols.remove(i)
                diagonal.remove(row+i)
                negDiagonal.remove(row-i)
                l.pop()
            
        res = []
        l = []
        cols,diagonal,negDiagonal = set(),set(),set()
        bt()
        return res 
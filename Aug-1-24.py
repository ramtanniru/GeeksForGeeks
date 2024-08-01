class Solution:
    def spirallyTraverse(self, matrix):
        l,r,t,b = 0,len(matrix[0])-1,0,len(matrix)-1
        res = []
        vis = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        while l<=r and t<=b:
            for i in range(l,r+1):
                if not vis[t][i]:
                    vis[t][i] = True
                    res.append(matrix[t][i])
            t += 1
            for i in range(t,b+1):
                if not vis[i][r]:
                    vis[i][r] = True
                    res.append(matrix[i][r])
            r -= 1
            for i in range(r,l-1,-1):
                if not vis[b][i]:
                    vis[b][i] = True
                    res.append(matrix[b][i])
            b -= 1
            for i in range(b,t-1,-1):
                if not vis[i][l]:
                    vis[i][l] = True
                    res.append(matrix[i][l])
            l += 1
        return res 
class Solution:
    def merge(self, root1, root2):
        def inL(root):
            nonlocal r1
            if not root:
                return
            inL(root.left)
            r1 += [root.data]
            inL(root.right)
        def inR(root):
            nonlocal r2
            if not root:
                return
            inR(root.left)
            r2 += [root.data]
            inR(root.right)
        r1 = []
        r2 = []
        inL(root1)
        inR(root2)
        res = []
        i,j = 0,0
        while i<len(r1) and j<len(r2):
            if r1[i]<r2[j]:
                res.append(r1[i])
                i += 1
            else:
                res.append(r2[j])
                j += 1
        while i<len(r1):
            res.append(r1[i])
            i += 1
        while j<len(r2):
            res.append(r2[j])
            j += 1
            
        return res 
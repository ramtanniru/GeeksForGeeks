class Solution:
    def KDistance(self,root,k):
        res = []
        def traverse(root,c):
            if not root:
                return
            if k==c:
                res.append(root.data)
                return
            traverse(root.left,c+1)
            traverse(root.right,c+1)
        traverse(root,0)
        return res
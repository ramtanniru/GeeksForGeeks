class Solution:
    def hasPathSum(self, root, target):
        def preOrder(root,s = 0):
            nonlocal res
            if not root:
                return
            s += root.data
            if not root.left and not root.right:
                if s==target:
                    res = True
                return
            preOrder(root.left,s)
            preOrder(root.right,s)
            s -= root.data
        res = False
        preOrder(root)
        return res  
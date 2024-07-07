class Solution:
    def __init__(self):
        self.res = []
    def Ancestors(self, root, target):
        def preOrder(root,t,res=[]):
            if not root:
                return
            if root.data==t:
                self.res=res.copy()
                return 
            res.append(root.data)
            preOrder(root.left,t,res)
            preOrder(root.right,t,res)
            res.pop()
            return 
        preOrder(root,target)
        return self.res[::-1]  
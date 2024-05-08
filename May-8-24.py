class Solution:
    def __init__(self):
        self.res = []
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        def dfs(root,stk = []):
            if not root:
                return
            stk.append(root.data)
            if not root.left and not root.right:
                self.res.append(stk.copy())
                stk.pop()
                return
            dfs(root.left,stk)
            dfs(root.right,stk)
            if stk:
                stk.pop()
            return
        dfs(root)
        return self.res
class Solution:
    def mirror(self,root):
        def pre(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            pre(root.left)
            pre(root.right)
        pre(root)
        return root 
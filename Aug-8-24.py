class Solution:
    def is_sum_tree(self, node):
        def postOrder(root):
            if not root:
                return (True,0)
            if not root.left and not root.right:
                return (True,root.data)
            isLeftSum,left = postOrder(root.left)
            isRightSum,right = postOrder(root.right)
            if isLeftSum and isRightSum and root.data==left+right:
                return (True,root.data+left+right)
            return (False,root.data+left+right)
        res = postOrder(node)
        return res[0] 
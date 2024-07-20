class Solution:
    def RemoveHalfNodes(self, node):
        def isHalfNode(root):
            if not root:
                return False
            if not root.left and not root.right:
                return False
            if not root.left or not root.right:
                return True
            return False
        def preOrder(root):
            if not root:
                return
            if isHalfNode(root):
                return preOrder(root.left) if root.left else preOrder(root.right)
            if isHalfNode(root.left):
                root.left = root.left.left if root.left.left else root.left.right
            if isHalfNode(root.right):
                root.right = root.right.left if root.right.left else root.right.right
            root.left = preOrder(root.left)
            root.right = preOrder(root.right)
            return root
        return preOrder(root) 
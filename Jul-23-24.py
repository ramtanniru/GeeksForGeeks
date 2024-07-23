class Solution:
    def merge(self, root1, root2):
        def inOrder(root,res=[]):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.data]
            l = inOrder(root.left)
            r = inOrder(root.right)
            return l+[root.data]+r 
        bst1 = inOrder(root1)
        bst2 = inOrder(root2)
        res = []
        i,j = 0,0
        while i<len(bst1) and j<len(bst2):
            if bst1[i]<bst2[j]:
                res.append(bst1[i])
                i += 1
            else:
                res.append(bst2[j])
                j += 1
        while i<len(bst1):
            res.append(bst1[i])
            i += 1
        while j<len(bst2):
            res.append(bst2[j])
            j += 1
        return res 
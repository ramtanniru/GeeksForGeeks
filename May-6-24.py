def noSibling(root):
    res = []
    def single(root):
        if not root:
            return
        single(root.left)
        single(root.right)
        if root and not root.left or not root.right:
            if root.left and not root.right:
                res.append(root.left.data)
            if root.right and not root.left:
                res.append(root.right.data)
    single(root)
    if res:
        res.sort()
        return res
    return [-1]
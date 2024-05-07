def reverseLevelOrder(root):
    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left),height(root.right))
    h = height(root)
    res = [[] for i in range(h)]
    def levelOrder(root):
        for i in range(1,h+1):
            sameLevelNodes(root,i,i-1)
    def sameLevelNodes(root,l,k):
        if not root:
            return
        if l==1:
            res[k].append(root.data)
        elif l>1:
            sameLevelNodes(root.left,l-1,k)
            sameLevelNodes(root.right,l-1,k)
    levelOrder(root)
    ans = []
    for i in res[::-1]:
        ans.extend(i)
    return ans
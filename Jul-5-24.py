def verticalWidth(root):
    def topView(root,hd,level,d):
        if not root:
            return
        if hd not in d:
            d[hd] = level
        elif d[hd]>level:
            d[hd] = level
        topView(root.left,hd-1,level+1,d)
        topView(root.right,hd+1,level+1,d)
    d = {}
    topView(root,0,0,d)
    return len(d) 

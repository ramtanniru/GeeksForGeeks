class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        def LeastCommonAncestor(root,x,y):
            if(root==None):
                return None;
            if(root.data<x and root.data<y):
                return LeastCommonAncestor(root.right,x,y)
            if(root.data>x and root.data>y):
                return LeastCommonAncestor(root.left,x,y)
            return root
        LCA = LeastCommonAncestor(root,x,y)
        curr = root
        path = []
        if LCA is None:
            return -1
        while(curr.data!=LCA.data):
            path.append(curr.data)
            if(curr.data>LCA.data):
                curr = curr.left
            else:
                curr = curr.right
        path.append(curr.data)
        if(len(path)<k):
            return -1
        return path[-k]
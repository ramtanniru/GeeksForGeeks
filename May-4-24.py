class Solution:
    def buildTree(self,In, post, n):
        if not In:
            return
        root = Node(post[-1])
        rootIndex = In.index(post[-1])
        post.pop(-1) 
        root.right = self.buildTree(In[rootIndex+1:],post,n)
        root.left = self.buildTree(In[:rootIndex],post,n)
        return root
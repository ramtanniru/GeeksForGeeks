class Solution:
    #Complete the function below
    def verticalSum(self, root):
        def maxDepth(root):
            if not root:
                return 0
            return 1+max(maxDepth(root.left),maxDepth(root.right))
        depth = maxDepth(root)
        dp = [0]*((2*depth)-1)
        def vSum(root,idx):
            if not root:
                return
            dp[idx] += root.data
            if root.left:
                vSum(root.left,idx-1)
            if root.right:
                vSum(root.right,idx+1)
        vSum(root,depth-1)
        res = []
        i,j = 0,len(dp)-1
        while i<len(dp):
            if dp[i]!=0:
                break
            i += 1
        while j>0:
            if dp[j]!=0:
                break
            j -= 1
        return dp[i:j+1]
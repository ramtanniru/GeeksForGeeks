class Solution:
    def treePathSum(self,root):
        def solve(path):
            temp = 0
            for i in path[:-1]:
                temp += i
                temp *= 10
            temp += path[-1]
            return temp
        def dfs(node=root,path=[root.data]):
            nonlocal ans
            if not node.left and not node.right:
                ans += solve(path)
                return
            if node.left:
                dfs(node.left,path+[node.left.data])
            if node.right:
                dfs(node.right,path+[node.right.data])
        ans = 0
        dfs()
        return ans
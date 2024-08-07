class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        mid = len(nums)//2
        root = Tree(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root 
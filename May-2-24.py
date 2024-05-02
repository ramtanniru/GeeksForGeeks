class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        if not root:
            return
        res = [[],root.data,[]]
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        if left:
            res[0].extend(left)
        if right:
            res[2].extend(right)
        return res
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        if not a:
            return
        root = Node(a[1])
        left = self.deSerialize(a[0])
        right = self.deSerialize(a[2])
        root.left = left
        root.right = right
        return root
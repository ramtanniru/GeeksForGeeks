class Solution:
    def __init__(self):
        self.prev = None

    def populateNext(self, root):
        if not root:
            return
        self.populateNext(root.left)
        if self.prev:
            self.prev.next = root
        self.prev = root
        self.populateNext(root.right)
        pass 

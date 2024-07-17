class Solution:
    def __init__(self):
        self.d = dict()
        self.s = set()
    def createTree(self,parent):
        for i in range(len(parent)):
            self.d[i] = Node(i)
        root = None
        for i,x in enumerate(parent):
            if x!=-1:
                if x not in self.s:
                    self.d[x].left = self.d[i]
                    self.s.add(x)
                else:
                    self.d[x].right = self.d[i]
            else:
                root = self.d[i]
        return root 
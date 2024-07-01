from collections import deque
#Function to make binary tree from linked list.
def convert(head):
    d = []
    curr = head
    while curr:
        d.append(curr.data)
        curr = curr.next
    # level order to binary tree 
    Q = deque([])
    def insert(root,data):
        newNode = Tree(data)
        if Q:
            temp = Q[0]
        if not root:
            root = newNode
        elif not temp.left:
            temp.left = newNode
        elif not temp.right:
            temp.right = newNode
            Q.popleft()
        Q.append(newNode)
        return root
    root = None
    for i in d:
        root = insert(root,i)
    return root 
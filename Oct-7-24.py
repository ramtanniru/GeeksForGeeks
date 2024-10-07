from collections import defaultdict
cache = defaultdict()

def insert(head, data):
    if id(head) not in cache:
        cache[id(head)] = head
    newNode = Node(data)
    cache[id(newNode)] = newNode
    newNode.npx = id(newNode)^id(head)
    return newNode
    
def getList(head):
    curr = head
    res = []
    while curr:
        res.append(curr.data)
        curr = cache[curr.npx^id(curr)]
    return res 
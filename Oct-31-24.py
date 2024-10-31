class Solution:
    def sortedInsert(self, head, x):
        curr = head
        newNode = Node(x)
        if curr.data>=x:
            newNode.next = head
            head.prev = newNode
            return newNode
        while curr and curr.next:
            if curr.next.data>=x:
                newNode.next = curr.next
                newNode.prev = curr
                curr.next = newNode
                newNode.next.prev = newNode
                return head
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr
        return head
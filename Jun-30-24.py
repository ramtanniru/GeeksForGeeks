class Solution:
    def delete_node(self, head, x):
        pos = 1
        curr = head
        if x==1:
            curr = curr.next
            return curr
        while curr and pos<x-1:
            curr = curr.next
            pos += 1
        if not curr.next.next:
            curr.next = None
            return head
        temp = curr.next.next
        temp.prev = curr
        curr.next = temp
        
        return head 
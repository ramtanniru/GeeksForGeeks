class Solution:
    def addOne(self,head):
        def reverse(node):
            dummy = Node(0)
            prev = dummy
            curr = node
            temp = node.next
            
            while temp:
                curr.next = prev
                prev = curr
                curr = temp
                if temp:
                    temp = temp.next
            curr.next = prev
            
            temp = curr
            while temp.next.next:
                temp = temp.next
            temp.next = None
            
            return curr
            
        newHead = reverse(head)
        curr = newHead
        
        carry = 1
        while curr:
            if curr.data<9:
                curr.data += carry
                carry = 0
                break
            curr.data = 0
            curr = curr.next
            carry = 1
        
        updatedHead = reverse(newHead)
        if carry:
            res = Node(1)
            res.next = updatedHead
            return res
        return updatedHead 
class Solution:
    def alternatingSplitList(self, head):
        lHead,rHead = Node(-1),Node(-1)
        curr = head
        l,r = lHead,rHead
        while curr:
            l.next = curr
            r.next = curr.next
            if curr.next:
                curr.next = curr.next.next
            curr = curr.next
            l = l.next
            r = r.next
        return lHead.next,rHead.next
class Solution:
    def findMid(self, head):
        s,f = head,head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s.data 
class Solution:
    def deleteAlt(self, head):
        curr = head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head
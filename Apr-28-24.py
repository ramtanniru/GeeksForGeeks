class Solution:
    def deleteMid(self,head):
        slow = fast = head
        while fast.next.next and fast.next.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
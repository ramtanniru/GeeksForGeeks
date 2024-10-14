class Solution:
    def getCount(self, head):
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        return l
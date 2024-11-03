class Solution:
    def isLengthEven(self, head):
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        return n&1==0
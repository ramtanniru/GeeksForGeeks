class Solution:
    def sumOfLastN_Nodes(self, head, n):
        l = 0
        curr = head
        s = 0
        while curr:
            s += curr.data
            curr = curr.next
            l += 1
        temps = 0
        curr = head
        while curr and l-n>0:
            temps += curr.data
            curr = curr.next
            n += 1
        return s-temps
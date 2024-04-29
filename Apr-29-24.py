class Solution:
    def deleteK(self, head, k):
        curr,i = head,1
        if k==1:
            return 
        while curr and curr.next:
            if i==k-1:
                curr.next = curr.next.next
                i = 0
            curr = curr.next
            i += 1
        return head
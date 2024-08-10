class Solution:
    def rotate(self, head, k):
        def findLength(head):
            curr = head
            res = 0
            while curr:
                res += 1
                curr = curr.next
            return res 
        k = k%findLength(head)
        if k==0:
            return head 
        temp = head
        curr = head
        cnt = 1
        while cnt<k:
            cnt += 1
            curr = curr.next
        temp = curr.next
        curr.next = None
        curr = temp
        while curr.next:
            curr = curr.next
        curr.next = head
        return temp 
    
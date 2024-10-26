class Solution:
    def count(self, head, key):
        res = 0
        curr = head
        while curr:
            if curr.data==key: res += 1
            curr = curr.next
        return res
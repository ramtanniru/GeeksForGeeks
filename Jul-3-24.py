import collections 
class Solution:
    def removeAllDuplicates(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        d = collections.Counter(arr)
        if arr:
            x = Node(0)
            curr = x
            for i in arr:
                if d[i]==1:
                    curr.next = Node(i)
                    curr = curr.next
            return x.next
        return 
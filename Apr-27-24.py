class Solution():
    def sortDoubly(self,head):
        l = []
        curr = head
        while curr.next:
            l.append(curr.data)
            temp = curr
            curr = curr.next
            curr.prev = temp
        l.append(curr.data)
        curr = head
        l.sort()
        i = 0
        while curr.next and i<len(l):
            curr.data = l[i]
            temp = curr
            curr = curr.next
            curr.prev = temp
            i+=1
        curr.data = l[i]
        return head
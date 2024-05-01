class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        vowels = {'a','e','i','o','u'}
        con,vow = [],[]
        curr = head
        while curr:
            i = curr.data
            curr = curr.next
            if i in vowels:
                vow.append(i)
            else:
                con.append(i)
        curr = head
        vow.extend(con)
        i = 0
        while curr:
            curr.data = vow[i]
            i += 1
            curr = curr.next
        return head
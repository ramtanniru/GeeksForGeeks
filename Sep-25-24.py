class Solution:
    def isPalindrome(self, head):
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        a = 0
        b = 0
        i = 0
        flag = True
        curr = head
        while i<n//2:
            if flag:
                a += int(curr.data)
                flag = False
            else:
                a -= int(curr.data)
                flag = True
            curr = curr.next
            i += 1
        if n%2!=0:
            if flag:
                a += int(curr.data)
            else:
                a -= int(curr.data)
        flag = True
        while i<n:
            if flag:
                b += int(curr.data)
                flag = False
            else:
                b -= int(curr.data)
                flag = True
            i += 1
            curr = curr.next
        return abs(a)==abs(b) 
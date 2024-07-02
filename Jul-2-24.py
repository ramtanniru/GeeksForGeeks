def compute(head): 
    s = ""
    curr = head
    while curr:
        s += curr.data
        curr = curr.next
    return s==s[::-1] 
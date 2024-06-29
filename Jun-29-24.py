def areIdentical(head1, head2):
    curr1,curr2 = head1,head2
    while curr1 and curr2:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    if curr1 or curr2:
        return False
    return True 
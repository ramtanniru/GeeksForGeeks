def intersetPoint(head1,head2):
    a,b = head1,head2
    l1,l2 = 0,0
    while a:
        a = a.next
        l1 += 1
    while b:
        b = b.next
        l2 += 1
    a,b = head1,head2
    if l1>l2:
        diff = l1-l2
        while diff>0:
            a = a.next
            diff -= 1
        if a.next:
            return a.next.data
    elif l1<l2:
        diff = l2-l1
        while diff>0:
            b = b.next
            diff -= 1
        if b.next:
            return b.next.data
    else:
        while a!=b:
            a = a.next
            b = b.next
        return a.data
    return -1
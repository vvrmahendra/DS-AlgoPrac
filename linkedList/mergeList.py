from linkedList import ListNode

def mergeTwoLists( A, B):
    if A == None:
        return B
    if B == None:
        return A    
    first = A
    second = B
    if A.val <= B.val:
        out = ListNode(A.val)
        first = first.next
    else:
        out = ListNode(B.val)
        second = second.next
        
    temp = out    
    while first != None and second != None:
        if first.val <= second.val:
            new = ListNode(first.val)
            temp.next = new
            temp = temp.next
            first = first.next
        else:
            new = ListNode(second.val)
            temp.next = new
            temp = temp.next
            second = second.next       
    while first != None:
        new = ListNode(first.val)
        temp.next = new
        temp = temp.next
        first = first.next
        
    while second != None:
        new = ListNode(second.val)
        temp.next = new
        temp = temp.next
        second = second.next
        
    return out


if __name__ == "__main__":
    pass
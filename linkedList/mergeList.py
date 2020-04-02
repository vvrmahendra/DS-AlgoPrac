from linkedList import ListNode
#saving the original list ans creating new nodes
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


#with no extra space
def mergeTwoListsV2(A, B):
    if not A:
        return B
    if not B:
        return A
        
    first = A
    second = B
    if first.val < second.val:
        ans = first
        first = first.next
    else:
        ans = second
        second = second.next
    temp = ans    
    while first and second:
        if first.val < second.val:
            temp.next = first
            first = first.next
            temp = temp.next
        else:
            temp.next = second
            second = second.next
            temp = temp.next
            
    if first:
        temp.next = first
    if second:
        temp.next = second
        
    return ans

if __name__ == "__main__":
    pass
"""Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 

For example, Given 1->2->3->3->4->4->5, return 1->2->5. Given 1->1->1->2->3, return 2->3."""

def deleteDuplicates(A):
    if not A:
        return A
    if not A.next:
        return A
        
    pre = None
    ans = None
    cur = A
    while cur:
        count  = 0
        value = cur.val
        temp = cur
        while cur and cur.val == value:
            cur = cur.next
            count += 1
        # print(count)    
        if count == 1:
            if not pre:
                pre = temp
                ans = pre
                pre.next = None
            else:
                pre.next = temp
                pre = pre.next
                pre.next =  None
                
    return ans
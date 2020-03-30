"""Cloning linked list with next and random next using no extra space"""
"""
class ListNode: 
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""
def clonelist(A):
    temp = A
    while temp:
        new = ListNode(temp.val)
        next = temp.next
        temp.next = new
        new.next = next
        temp = next
        
    temp = A    
    while temp:
        temp.next.random = temp.random.next
        temp = temp.next.next
        
    first = A
    ans = A.next
    second = A.next
    while first:
        first.next = first.next.next
        second.next = second.next.next if second.next else None
        first = first.next
        second = second.next
        
    return ans

#This takes O(n) space. Using recurstion
def clonelistRecursion(A):
    import sys
    sys.setrecursionlimit(15000)
    dict_ = {}
    def helper(head):
        if not head:
            return head
            
        if head in dict_:
            return dict_[head]
            
        new = ListNode(head.val)    
        dict_[head] = new
        
        new.next = helper(head.next)
        new.random = helper(head.random)
        
        return dict_[head]
    return helper(A)
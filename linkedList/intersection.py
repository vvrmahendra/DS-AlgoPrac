"""Intersection of Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins. For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1."""

"We can first calculate lengths of both list and can parse from starting based on the list lingths"
"But here I appraoched entirely diffeent appraoch. Which is creating a loop and finding out the starting point of the loop"



def getIntersectionNode(A, B):
    if not A or not B:
        return None
    first = A
    while first.next:
        first = first.next
    end = first
    first.next = B

    if A:
        slow = A.next
    else:
        return None
        
    if A.next:
        fast = A.next.next
    else:
        return None
        
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
        
    if not fast or not fast.next:
        return None
    
    slow = A
    while slow != fast:
        slow = slow.next
        fast = fast.next
    while slow != end:
        slow = slow.next
        
    slow.next = None
    return fast
    
"""Reorder List
Problem Description
Given a singly linked list A
 A: A0 → A1 → … → An-1 → An 
reorder it to:
 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values. 


Problem Constraints
1 <= |A| <= 106


Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.


Output Format
Return a pointer to the head of the modified linked list.


Example Input
Input 1:
 A = [1, 2, 3, 4, 5] 
Input 2:
 A = [1, 2, 3, 4] 


Example Output
Output 1:
 [1, 5, 2, 4, 3] 
Output 2:
 [1, 4, 2, 3] 


Example Explanation
In the first example, the array will be arranged to [A0, An, A1, An-1, A2]. In the second example, the array will be arranged to [A0, An, A1, An-1]"""


def reorderList(A):
    if not A:
        return A
        
    if not A.next:
        return A
        
    fast = A
    slow = A
    while fast and fast.next:
        fast = fast.next.next
        pre = slow
        slow = slow.next
        
    if fast:    
        mid = slow
    else:
        mid = pre
    second = mid.next
    mid.next = None
    pre = None
    cur = second
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        
    second = pre
    
    temp1 = A
    temp2 = second
    
    while temp2:
        pla1 = temp1.next
        pla2 = temp2.next
        temp1.next = temp2
        
        temp2.next = pla1
        temp1 = pla1
        temp2 = pla2
        
    return A
        
    
    
    
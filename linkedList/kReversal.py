"""K reverse linked list
Problem Description
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.


Problem Constraints
1 <= |A| <= 103 K always divides A     


Input Format
The first argument of input contains a pointer to the head of the linked list. The second arugment of input contains the integer, B.     


Output Format
Return a pointer to the head of the modified linked list.


Example Input
Input 1:
 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:
 A = [1, 2, 3, 4, 5, 6]
 B = 3
    


Example Output
Output 1:
 [2, 1, 4, 3, 6, 5]
Output 2:
 [3, 2, 1, 6, 5, 4]"""

def reverseList(A, B):
    if B == 1:
        return A
    cur  =  A
    pre = None
    for _ in range(B):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    
    if not next:
        A.next = None
        return pre
        
    A.next = self.reverseList(cur, B)
    return pre
Remove Duplicates from Sorted List"""
Problem Description
Given a sorted linked list, delete all duplicates such that each element appear only once.


Problem Constraints
0 <= length of linked list <= 1000000


Input Format
First argument is the head pointer of the linked list.


Output Format
Return the head pointer of the linked list after removing all duplicates.


Example Input
Input 1:
1->1->2
Input 2:
1->1->2->3->3
 


Example Output
Output 1:
1->2
Output 2:
1->2->3
 


Example Explanation
Explanation 1:
each element appear only once in 1->2."""

def deleteDuplicates(A):
    if not A:
        return A
    temp = A
    while temp:
        uni = temp
        curVal = uni.val
        while temp and temp.val == curVal:
            temp = temp.next
            
        if not temp:
            uni.next = None
            return A
        if temp != uni:
            uni.next = temp

        
        
    return A
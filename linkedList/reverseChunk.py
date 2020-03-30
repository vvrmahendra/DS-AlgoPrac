"""Problem Description
Reverse a linked list A from position B to C. NOTE: Do it in-place and in one-pass. 


Problem Constraints
1 <= |A| <= 106 1 <= B <= C <= |A| 


Input Format
The first argument contains a pointer to the head of the given linked list, A. The second arugment contains an integer, B. The third argument contains an integer C. 


Output Format
Return a pointer to the head of the modified linked list.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 2
C = 4
Input 2:
A = [1, 2, 3, 4, 5]
B = 1
C = 5


Example Output
Output 1:
[1, 4, 3, 2, 5]
Output 2:
[5, 4, 3, 2, 1]"""

def reverseBetween(A, B, C):
    if B == C:
        return A
    if B == 1:
        chunk_end = None
    else:
        chunk_end = A
        for i in range(B-2):
            chunk_end = chunk_end.next
    
    pre = None
    second_chunk = chunk_end.next if chunk_end else A
    cur = second_chunk
    for i in range(C-B+1):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        
    if chunk_end:    
        chunk_end.next = pre
    second_chunk.next = cur 
    
    return A if chunk_end else pre
"""Hide boxes
Problem Description
There are N cubical boxes and the edge length of boxes is given by an array A of size N. A box can hold another box inside it, if and only if the length of a box is at least twice as large than another box. There can be atmost one box inside any other box. The box which is inside another box is not visible. You have to minimize the number of boxes visible.  


Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 109


Input Format
First argument is an integer array A of size N.


Output Format
Return an integer denoting minimum number of boxes visible.


Example Input
 A = [1, 2, 2, 4, 3]


Example Output
 3


Example Explanation
 We can put the box at index 1 into box at index 5.Also, the box at index 2 into box at index 4. 
 So, the visible boxes will be the box at index 3,4,5.
"""




def solve(A):
    A.sort()
    n = len(A)
    first_half = (n+1)//2
    i = 0
    j = first_half
    ans = 0
    while i < first_half and j < n:
        if 2*A[i] <= A[j]:
            ans += 1
            i += 1
            j += 1
        elif 2*A[i] > A[j]:
            ans += 1
            j += 1
            
    while i < first_half:
        i += 1
        ans += 1
        
    while j < n:
        j += 1
        ans += 1
    return ans
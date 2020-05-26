"""Matrix and Absolute Difference
Problem Description
Given a matrix C of integers, of dimension A x B. For any given K, you are not allowed to travel between cells that have an absolute difference greater than K. Return the minimum value of K such that it is possible to travel between any pair of cells in the grid through a path of adjacent cells. NOTE:
Adjacent cells are those cells that share a side with the current cell.
 


Problem Constraints
1 <= A, B <= 102 1 <= C[i][j] <= 109  


Input Format
The first argument given is A. The second argument give is B. The third argument given is the integer matrix C.  


Output Format
Return a single integer, the minimum value of K.


Example Input
Input 1:
 A = 3
 B = 3
 C = [  [1, 5, 6]
        [10, 7, 2]
        [3, 6, 9]   ]
 


Example Output
Output 1:
 4
 


Example Explanation
Explanation 1:
 
 It is possible to travel between any pair of cells through a path of adjacent cells that do not have an absolute
 difference in value greater than 4. e.g. : A path from (0, 0) to (2, 2) may look like this:
 => (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)"""


from heapq import *
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        heap = []
        for i in range(B-1):
            w,l,r = abs(C[0][i+1]-C[0][i]), i, i+1
            heap.append((w,l,r))
        for i in range(A-1):
            w,l,r = abs(C[i+1][0]-C[i][0]), i*B, (i+1)*B
            heap.append((w,l,r))
            
        for i in range(1,A):
            for j in range(1,B):
                w,l,r = abs(C[i][j] - C[i-1][j]), i*B+j, (i-1)*B+j
                heap.append((w,l,r))
                
                w,l,r = abs(C[i][j] - C[i][j-1]), i*B+j, i*B+j-1
                heap.append((w,l,r))
        heapify(heap)
        p = [i for i in range(A*B)]
        s = [1]*(A*B)
        
        edge = 0
        ans = float('-inf')
        while edge < A*B-1:
            w, l, r = heappop(heap)
            
            pl = l
            while pl != p[pl]:
                pl = p[pl]
                
            pr = r
            while pr != p[pr]:
                pr = p[pr]
                
            if pl == pr:
                continue
            
            edge += 1
            ans = max(ans, w)
            if s[pl] >= s[pr]:
                p[pr] = pl
                s[pl] += s[pr]
                
            else:
                p[pl] = pr
                s[pr] += s[pl]
                
        return ans
        
"""Commutable Islands
Problem Description
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it. We need to find bridges with minimal cost such that all islands are connected. It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other. 


Problem Constraints
1 <= A, M <= 6*104 1 <= B[i][0], B[i][1] <= A 1 <= B[i][2] <= 103 


Input Format
The first argument contains an integer, A, representing the number of islands. The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2]. 


Output Format
Return an integer representing the minimal cost required.


Example Input
Input 1:
 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:
 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output
Output 1:
 6
Output 2:
 6


Example Explanation
Explanation 1:
 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.
Explanation 2:
 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6."""

from heapq import *
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        heap = []
        ans = [0]*(len(B))
        for i, ray in enumerate(B):
            l, r, w = ray
            heap.append((w,l,r,i))
            
        heapify(heap)
        p = [i for i in range(A+1)]
        s = [1]*(A+1)
        
        while heap:
            w,l,r,i = heappop(heap)
            pl = l
            while pl != p[pl]:
                pl = p[pl]
                
            pr = r
            while pr != p[pr]:
                pr = p[pr]
                
            if pl == pr:
                continue
            
            ans[i] = 1
            if s[pl] >= s[pr]:
                p[pr] = pl
                s[pl] += s[pr]
            else:
                p[pl] = pr
                s[pr] += s[pl]
            
            
            
        return sum((B[i][-1] for i in range(len(B)) if ans[i]))
                
                
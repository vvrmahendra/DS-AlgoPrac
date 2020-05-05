"""Interleaving Strings
Problem Description
Given A, B, C, find whether C is formed by the interleaving of A and B.


Problem Constraints
1 <= length(A), length(B) <= 100 1 <= length(C) <= 150 


Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.


Output Format
Return 1 if string C is formed by interleaving of A and B else 0.


Example Input
Input 1:
 A = "aabcc"
 B = "dbbca"
 C = "aadbbcbcac"
Input 2:
 A = "aabcc"
 B = "dbbca"
 C = "aadbbbaccc"
 


Example Output
Output 1:
 1
Output 2:
 0
 


Example Explanation
Explanation 1:
 "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)
Explanation 2:
 It is not possible to get C by interleaving A and B."""

from functools import lru_cache
class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):
        
        @lru_cache(maxsize=None)
        def helper(p1,p2,p3):
            if p1 == len(A):
                return B[p2:] == C[p3:]
            
            if p2 == len(B):
                return A[p1:] == C[p3:]
                
            if p3 == len(C):
                return len(A) == p1 and len(B) == p2
            
            if A[p1] == C[p3]:
                first =  helper(p1+1, p2, p3+1)
            else:
                first = False
                
            if B[p2] == C[p3]:
                second =  helper(p1, p2+1, p3+1)
            else:
                second = False
                
            
                
            return first or second
                
        return int(helper(0,0,0))
            
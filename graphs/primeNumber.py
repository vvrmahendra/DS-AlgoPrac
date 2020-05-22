"""Smallest sequence with given Primes
Problem Description
Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.


Problem Constraints
1 <= A, B, C <= 10000 1 <= D <= 100000 


Input Format
First argument is an integer A.
Second argument is an integer B.
Third argument is an integer C.
Fourth argument is an integer D.


Output Format
Return an integer array of size D, denoting the first D integers described above. NOTE: The sequence should be sorted in ascending order 


Example Input
Input 1:
 A = 2
 B = 3
 C = 5
 D = 5
Input 2:
 A = 3
 B = 2
 C = 7
 D = 3


Example Output
Output 1:
 [2, 3, 4, 5, 6]
Output 2:
 [2, 3, 4]


Example Explanation
Explanation 1:
 4 = A * A ( 2 * 2 ), 6 = A * B ( 2 * 3 )
Explanation 2:
 2 has only prime factor 2. Similary 3 has only prime factor 3. 4 = A * A ( 2 * 2 )"""


from heapq import *
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
	def solve(self, A, B, C, D):
        A,B,C = sorted([A,B,C])
        list_ = [A]
        if A!= B: list_.append(B)
        if B!= C: list_.append(C)
        ans = []
        heap = [(a,a) for a in list_]
        heapify(heap)
        for i in range(D):
            cur, min_ = heappop(heap)
            ans.append(cur)
            for ele in list_:
                if min_ <= ele:
                    heappush(heap,(cur*ele, ele))
        
        return ans
	        


#dp implementaion... i have implemented same using greedy algorithm in greedy section
#refer there for problem statement
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
        n = len(A)
        if n == 0: return 0
        if n==1: return A[0]
        max_end_here = 1
        min_end_here = 1
        max_so_far = 1
        for i in A:
            if i > 0:
                max_end_here *= i
                min_end_here = min(min_end_here*i, 1)
                
            elif i == 0:
                max_end_here = 1
                min_end_here = 1
            else:
                temp = min_end_here
                min_end_here = max_end_here*i
                max_end_here = max(1, temp*i)
                
            max_so_far = max(max_so_far, max_end_here)
            
        if max_so_far == 1:
            for i in A:
                if i == 1:
                    return 1
                    break
            else:
                return 0
                
        return max_so_far
                
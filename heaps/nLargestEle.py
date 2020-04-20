"""N max pair combinations
Given two arrays A & B of size N each. Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B. For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6 and maximum 2 elements are 6, 5 Example: N = 4 a[]={1,4,2,3} b[]={2,5,1,6}
Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)"""

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def solve(self, A, B):
        import heapq as hq
        ans = []
        A =  [-1*i for i in A]
        B =  [-1*i for i in B]
        A.sort()
        B.sort()
        heap = [(A[i]+B[0],i, 0) for i in range(len(A))]
        hq.heapify(heap)
        ans = []
        for _ in range(len(B)):
            # print(heap)
            temp, i, j = hq.heappop(heap)
            if j+1 < len(B):
                hq.heappush(heap, (A[i]+B[j+1], i, j+1))
            ans.append(-1*temp)
        return ans
        
"""Minimum largest element after K operations
Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation. Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Return an integer corresponding to the minimum possible largest element after K operations. Example:
Input : 
  A = [1, 2, 3, 4] 
  B = 3

Output : 4

Explanation : 
After the 1st operation the array would change to [2, 2, 3, 4]
After the 2nd operation the array would change to [3, 2, 3, 4]
After the 3rd operation the array would change to [4, 2, 3, 4]"""


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
        import heapq as hq
        heap = [(i+i,i) for i in A]
        hq.heapify(heap)
        for _ in range(B):
            temp = hq.heappop(heap)
            hq.heappush(heap, (temp[0]+temp[1], temp[1]))
        
        return max([i[0]-i[1] for i in heap])
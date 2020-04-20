"""Special Median
Median finding have always been an interesting task in programming. Sometimes we need to find medians repeatedly and this task requires an optimized algorithm for finding the median. Below is one such task: You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
Note:
For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
You need to output 1/0 (1 --> if array is special, 0 otherwise) Constraints: 0 <= N <= 1000000. A[i] is in the range of a signed 32-bit integer. Example:
Input:
A = [4, 6, 8, 4]

Output:
1
Here, 6 is equal to the median of [8, 4]."""



import heapq as hq
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def helper(self, A):
        n = len(A)
        maxHeap = []
        minHeap = []
        for i in range(n-1):
            if len(maxHeap) == len(minHeap):
                if minHeap and minHeap[0] < A[i]:
                    temp = hq.heappop(minHeap)
                    hq.heappush(minHeap, A[i])
                    hq.heappush(maxHeap, -1*temp)
                    if A[i+1] == -1*maxHeap[0]:
                        return 1
                        
                else:
                    hq.heappush(maxHeap, -1*A[i])
                    if A[i+1] == -1*maxHeap[0]:
                        return 1
                        
            else:
                if maxHeap and -1*maxHeap[0] > A[i]:
                    temp = hq.heappop(maxHeap)
                    hq.heappush(maxHeap, -1*A[i])
                    hq.heappush(minHeap, -1*temp)
                    if A[i+1] == (minHeap[0]-maxHeap[0])/2:
                        return 1
                else:
                    hq.heappush(minHeap, A[i])
                    if A[i+1] == (minHeap[0]-maxHeap[0])/2:
                        return 1
                        
        return 0
    def solve(self, A):
        n = len(A)
        if n <= 1:
            return int(not n)
            
        l = self.helper(A)
        r = self.helper(A[::-1])
        return 1 if l+r else 0
        
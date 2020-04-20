"""Median of stream of running integers
Given an array of integers A denoting a stream of integers. A new array of integer B is formed and C are formed. Each time an integer is encountered in a stream append it at the end of B and append median of array B at the C. Find and return the array C. NOTE: 1.If the number of elements are n in B and n is odd then consider medain as B[n/2] ( B must be in sorted order). 2.If the number of elements are n in B and n is even then consider medain as B[n/2-1] ( B must be in sorted order). 
Input Format
The only argument given is the integer array A.
Output Format
Return the array C.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 1000000000
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    C = [1, 1, 2, 2, 3]

    stream          median
    [1]             1
    [1, 2]          1
    [1, 2, 3]       2
    [1, 2, 3, 4]    2
    [1, 2, 3, 4, 5] 3

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    C = [5, 5, 17, 11]"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        import heapq as hq
        maxHeap = []
        minHeap = []
        ans = []
        for i in A:
            if len(maxHeap) == len(minHeap):
                if minHeap and minHeap[0] < i:
                    temp = hq.heappop(minHeap)
                    hq.heappush(minHeap, i)
                    hq.heappush(maxHeap, -1*temp)
                    ans.append(-1*maxHeap[0])
                else:
                    hq.heappush(maxHeap, -1*i)
                    ans.append(-1*maxHeap[0])
                    
            else:
                if maxHeap and  -1*maxHeap[0] > i:
                    temp = hq.heappop(maxHeap)
                    hq.heappush(maxHeap, -1*i)
                    hq.heappush(minHeap, -1*temp)
                    ans.append((0-maxHeap[0]))
                else:
                    hq.heappush(minHeap, i)
                    ans.append((0-maxHeap[0]))
                    
        return ans
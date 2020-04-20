"""Scooby likes the kth element
Scooby wants to help you as he knows that you are preparing for interviews. So Scooby gives you a very simple question.
You are given N numbers. You need to find the kth largest element in the subarray [1 to i] where i varies from 1 to N. In other words you need to find the kth largest element in the sub-arrays [1:1], [1:2], [1:3], ...., [1:n] . 
 Input:
1. The first argument given is an integer K.  
2. The second argument given is an array having N integers.  
Output:
Return an array X of size N, where X[i] (1 <= i <= N) will have the kth largest element in the subarray [1 to i].  
If a subarray has less than K elements then A[i] should be -1.  
Constraints:
1 <= N <= 100000  
1 <= K <= N  
Example:
Input:  

    K = 4  
    Array = [1 2 3 4 5 6]  

Output:  

    X = [-1 -1 -1 1 2 3] """

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        if A > len(B):
            return [-1]*len(B)
        ans = [-1]*(A-1)
        import heapq as hq
        heap = B[:A]
        hq.heapify(heap)
        temp = hq.heappop(heap)
        hq.heappush(heap,temp)
        ans.append(temp)
        j = A
        while j < len(B):
            if temp > B[j]:
                ans.append(temp)
            else:
                hq.heappop(heap)
                hq.heappush( heap, B[j])
                temp = hq.heappop(heap)
                hq.heappush(heap,temp)
                ans.append(temp)
            j += 1
            
        return ans
            
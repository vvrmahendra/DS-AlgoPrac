"""Remove elements
Problem Description
Given an integer array A of size N. In one operation, you can remove any element from the array and cost of this operation is sum of all elements in the array present before this operation. Find the minimum cost to remove all elements from the array. NOTE: Return the answer modulo 109 + 7 as the answer can be large.        


Problem Constraints
0 <= N <= 100000
0 <= A[i] <= 109


Input Format
First and only argument is an integer array A.


Output Format
Return an integer denoting the total cost of removing all elements from the array.


Example Input
Input 1:
 A = [2, 1]
Input 2:
 A = [5]
       


Example Output
Output 1:
 4
Output 2:
 5
       


Example Explanation
Explanation 1:
 Given array A = [2, 1]
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
 Remove 1 from the array => []. Cost of this operation is (1) = 1.
 So, total cost is = 3 + 1 = 4.
 
Explanation 2:
 There is only one element in the array. So, cost of removing is 5."""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        sum_ = sum(A)
        A = [-1*i for i in A]
        import heapq as hq
        hq.heapify(A)
        while A:
            ans += sum_
            temp = hq.heappop(A)
            sum_ += temp
        mod = 10**9+7    
        return ans%mod
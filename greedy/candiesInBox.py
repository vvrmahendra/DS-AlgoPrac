"""Candies in Box
Problem Description
There are 2 * N small boxes containing candies denoted by an integer array A of size 2 * N.  There are N-1 big boxes and each big box can accomodate exactly 2 small boxes. So, we can use exactly 2 * (N-1) small boxes. The cost of each big box is the absolute difference of candies in that box. For example: A big box contain two small boxes with candies 4 and 6 then the cost of this big box will be | 4 - 6 | = 2. You have to fill all the big boxes such that the total cost of big boxes are minimized. Find and return the minimum total cost of big boxes.   


Problem Constraints
1 <= N <= 50 1 <= A[i] <= 107   


Input Format
First argument is an integer array A of size 2 * N.


Output Format
Return an integer denoting the minimum total cost of big boxes.


Example Input
A = [2, 4, 1, 10, 6, 15]


Example Output
3


Example Explanation
Since 2 * N = 6. So there are 2 big boxes, we can place 4 small boxes inside the 2 big boxes.
Inorder to minimize the cost, we will select boxes with candies (2, 1) and (4, 6). So the minimum cost will be 2 + 1 =3."""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ans, n = float('inf'), len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                tempans = 0
                temp = A[:i]+A[i+1:j]+A[j+1:]
                for k in range(0,n-2,2):
                    first = temp[k]
                    second = temp[k+1]
                    tempans += abs(second-first)
                    
                ans = min(ans, tempans)
            
        return ans
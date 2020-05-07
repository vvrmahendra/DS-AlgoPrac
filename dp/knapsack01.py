"""0-1 Knapsack
Problem Description
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively. Also given an integer C which represents knapsack capacity. Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C. NOTE:
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


Problem Constraints
1 <= N <= 103 1 <= C <= 103 1 <= A[i], B[i] <= 103 


Input Format
First argument is an integer array A of size N denoting the values on N items. Second argument is an integer array B of size N denoting the weights on N items. Third argument is an integer C denoting the knapsack capacity. 


Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.


Example Input
Input 1:
 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50
Input 2:
 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10


Example Output
Output 1:
 220
Output 2:
 0


Example Explanation
Explanation 1:
 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
Explanation 2:
 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.
"""



from collections import defaultdict
import sys
sys.setrecursionlimit(15000)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = defaultdict(int)
        def helper(i,t):
            if (i,t) in dp:
                return dp[(i,t)]
                
            if i == len(A):
                return 0    
            if B[i] > t:
                if (i+1, t) in dp:
                    second = dp[(i+1,t)]
                else:
                    second = helper(i+1, t) 
                
                dp[(i,t)] = second
                return second
                
            
                
            if (i+1, t-B[i]) in dp:
                first = dp[(i+1, t-B[i])]
            else:
                first = helper(i+1, t-B[i])
            
            if (i+1, t) in dp:
                second = dp[(i+1,t)]
            else:
                second = helper(i+1, t)
                
            dp[(i,t)] = max(first+A[i], second)
            return dp[(i,t)]
            
        return helper(0,C)
        
        
"""Unbounded Knapsack
Problem Description
Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate minimum amount that could make up this quantity exactly. This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.    


Problem Constraints
1 <= A <= 1000 1 <= |B| <= 1000 1 <= B[i] <= 1000 1 <= C[i] <= 1000    


Input Format
First argument is the Weight of knapsack A Second argument is the vector of values B Third argument is the vector of weights C    


Output Format
Return the maximum value that fills the knapsack completely


Example Input
Input 1:
A = 10
B = [5]
C = [10]
  Input 2:            
A = 10
B = [6, 7]
C = [5, 5]
       


Example Output
Output 1:
 5
  Output 2:            
13
       


Example Explanation
Explanation 1:
Only valid possibility is to take the given item.
  Explanation 2:            
We can take both items.
"""

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        n = len(B)
        dp = [float('-inf')]*(A+1)
        dp[0] = 0
        for i in range(1,A+1):
            for ind, wt in enumerate(C):
                if wt <= i:
                    dp[i] = max(dp[i], dp[i-wt]+B[ind])
                    
        return dp[-1]
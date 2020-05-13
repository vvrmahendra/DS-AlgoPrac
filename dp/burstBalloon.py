"""Burst Balloons
Problem Description
You are given N balloons each with a number of coins associated with them. An array of integers A represents the coins associated with the ith balloon.
You are asked to burst all the balloons. If the you burst balloon ith you will get A[left] * A[i] * A[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent. Find the maximum coins you can collect by bursting the balloons wisely. NOTE: You may imagine A[-1] = A[N] = 1. They are not real therefore you can not burst them.  


Problem Constraints
1 <= N <= 100
1 <= A[i] <= 100


Input Format
The only argument given is the integer array A.


Output Format
Return the maximum coins you can collect by bursting the balloons wisely.


Example Input
Input 1:
 A = [3, 1, 5, 8]
Input 2:
 A = [3, 1, 2]
 


Example Output
Output 1:
 167
Output 2:
 15
 


Example Explanation
Explanation 1:
 Burst ballon at index 1, coins collected = 3*1*5=15 , A becomes = [3, 5, 8] 
 Burst ballon at index 1, coins collected = 3*5*8=120 , A becomes = [3, 8]
 Burst ballon at index 0, coins collected = 1*3*8=24 , A becomes = [8]
 Burst ballon at index 0, coins collected = 1*8*1 = 8
 Total coins collected = 15 + 120 + 24 + 8 = 167
Explanation 2:
 Burst ballon at index 1, coins collected = 3*1*2 = 6, A becomes = [3, 2] 
 Burst ballon at index 1, coins collected = 3*2*1 = 6, A becomes = [3]
 Burst ballon at index 0, coins collected = 1*3*1 = 3
 Total coins collected = 6 + 6 + 3 = 15"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.append(1)
        dp = [[0]*(n+1) for i in range(n+1)]
        for len_ in range(1,n+1):
            for f in range(n-len_+1):
                e = f+len_-1
                temp = float('-inf')
                for c in range(f,e+1):
                    
                    if c == f and c==e:
                        # print("first ",A[f:e+1], A[c],A[f:c],A[c+1:e+1])
                        temp = A[c]*A[f-1]*A[e+1]
                    elif c == f:
                        # print("second ",A[f:e+1], A[c],A[f:c],A[c+1:e+1])
                        temp = max(temp, dp[c+1][e]+A[c]*A[f-1]*A[e+1])
                    elif c == e:
                        # print("third ",A[f:e+1], A[c],A[f:c],A[c+1:e+1])
                        temp = max(temp, dp[f][c-1]+A[c]*A[f-1]*A[e+1])
                    else:
                        # print("fourth ",A[f:e+1], A[c],A[f:c],A[c+1:e+1])
                        temp = max(temp, dp[f][c-1]+dp[c+1][e]+A[c]*A[f-1]*A[e+1])
                        
                # print(temp)
                dp[f][e] = temp
        # print(dp)        
        return dp[0][n-1]
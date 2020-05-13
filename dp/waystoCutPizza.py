"""1444. Number of Ways of Cutting a Pizza
Hard

92

4

Add to List

Share
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only."""

# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

from functools import lru_cache
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9+7
        n, m = len(pizza), len(pizza[0])
        post = [[0]*(m+1) for _ in range(n+1)]
        post[n-1][m-1] = int(pizza[n-1][m-1] == 'A')
        for i in range(m-2,-1,-1):
            post[n-1][i] = post[n-1][i+1]+int(pizza[n-1][i] == 'A')
        for i in range(n-2,-1,-1):
            post[i][m-1] = post[i+1][m-1]+int(pizza[i][m-1] == 'A')
            
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                post[i][j] = post[i+1][j]+post[i][j+1]-post[i+1][j+1]+int(pizza[i][j] == 'A')
                
        @lru_cache(maxsize = None)        
        def helper(k,r,c):
            if post[r][c] == 0:
                return 0
            if k == 0:
                return 1
            
            ans = 0
            for i in range(r,n):
                if post[r][c]-post[i][c] > 0:
                    ans = (ans+helper(k-1, i,c))%mod
                    
            for j in range(c,m):
                if post[r][c]-post[r][j] > 0:
                    ans = (ans+helper(k-1, r,j))%mod
            return ans
        
        return helper(k-1, 0, 0)
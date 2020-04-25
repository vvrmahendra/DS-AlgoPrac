"""Ways to Decode
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it. 
Input Format:
The first and the only argument is a string A.
Output Format:
Return an integer, representing the number of ways to decode the string.
Constraints:
1 <= length(A) <= 1e5
Example :
Input 1:
    A = "8"

Output 1:
    1

Explanation 1:
    Given encoded message "8", it could be decoded as only "H" (8).

    The number of ways decoding "8" is 1.

Input 2:
    A = "12"

Output 2:
    2

Explanation 2:
    Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).

    The number of ways decoding "12" is 2.
"""

class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
        if len(A) == 1: return 1 if int(A) > 0 else 0
        n = len(A)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if int(A[0]) else 0
        for i in range(2,n+1):
            if A[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(A[i-2]+A[i-1]) <= 26:
                dp[i] += dp[i-2]
        # print(dp)        
        return dp[n]
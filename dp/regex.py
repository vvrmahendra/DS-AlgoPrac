"""Regular Expression Match
Problem Description
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.
' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).
 The matching should cover the entire input string (not partial).  


Problem Constraints
1 <= length(A), length(B) <= 104


Input Format
The first argument of input contains a string A.
The second argument of input contains a string B.


Output Format
Return 0 or 1:
=> 0 : If the patterns do not match.
=> 1 : If the patterns match.


Example Input
Input 1:
 A = "aaa"
 B = "a*"
Input 2:
 A = "acz"
 B = "a?a"
 


Example Output
Output 1:
 1
Output 2:
 0
 


Example Explanation
Explanation 1:
 Since '*' matches any sequence of characters. Last two 'a' in string A will be match by '*'.
 So, the pattern matches we return 1.
Explanation 2:
 '?' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0."""

# 2D dp Approach
class Solution2D:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        n, m = len(A), len(B)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1,m+1):
            if B[i-1] == '*':
                dp[0][i] = True
            else:
                break
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        for i in dp: print([int(ele) for ele in i])            
        return int(dp[-1][-1])

# 1D dp appraoch
class Solution1D:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        p = B
        s = A
        if len(p) - p.count('*') > len(s):
            return 0
        DP = [True] + [False]*len(s)
        for c in p:
            if c == '*':
                for n in range(1, len(s)+1):
                    DP[n] = DP[n-1] or DP[n]
            else:
                for n in range(len(s)-1, -1, -1):
                    DP[n+1] = DP[n] and (c == s[n] or c == '?')
            DP[0] = DP[0] and c == '*'
        return 1 if DP[-1] else 0
"""N digit numbers
Problem Description
Find out the number of A digit numbers, whose digits on being added equals to a given number B. Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed. Since the answer can be large, output answer modulo 1000000007     


Problem Constraints
A <= 1000 B <= 10000     


Input Format
First argument is the integer A Second argument is the integer B     


Output Format
Return a single integer, the answer to the problem


Example Input
Input 1:
 A = 2
 B = 4
Input 2:
 A = 1
 B = 3
 


Example Output
Output 1:
 4
  Output 2:
 1
 


Example Explanation
Explanation 1:
 Valid numbers are {22, 31, 13, 40}
 Hence output 4.
  Explanation 2:
 Only valid number is 3
"""


from functools import lru_cache
import sys
from collections import defaultdict
sys.setrecursionlimit(15000)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dict_ = defaultdict(int)
        def helper(d, s):
            if (d,s) in dict_:
                return dict_[(d,s)]
            if d == 1:
                if 0<=s<=9:
                    return 1
                else:
                    return 0
            ans = 0        
            for i in range(0,10):
                if d == A and i == 0:
                    continue
                if s >= i:
                    ans = (ans+helper(d-1, s-i))%1000000007
            
            dict_[(d,s)] = ans        
            return ans
            
        return helper(A,B)
                    

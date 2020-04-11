XOR QUERIES
Problem Description
Given three integers A, B and C. Return the maximum possible value of A ^ D, such that D is an integer in range [B, C]. Note 1: ^ repersents BITWISE xor. Note 2: A single testfile may contain multiple testcases upto 105.  


Problem Constraints
1 <= A, B, C <= 109


"""Input Format
The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer C.


Output Format
Return the maximum possible value of A ^ D, such that D is an integar in range [B, C].


Example Input
Input 1:
 A = 2
 B = 1
 C = 10
Input 2:
 A = 3
 B = 5
 C = 6
 


Example Output
Output 1:
 11
Output 2:
 6
 


Example Explanation
Explanation 1:
 For D = 9, A ^ D = 11, which is maximum for any D in range [1, 10].
Explanation 2:
 For D = 5, A ^ D = 6, which is maximum for any D in range [5, 6]
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        import math
        l = int(math.log2(C))
        x = 0
        for i in range(l, -1 ,-1):
            bit = A&(1<<i)
            if bit:# we will check if setting all of the next bits is enough to keep X >= L. If not, then we are required to set the current bit. Observe that setting all of the next bits is equivalent to adding (1 << b) – 1, where b is the current bit.
                if x+(1<<i)-1 < B:
                    x = x+(1<<i)
            else:
                if x+(1 << i) <= C:
                    x = x+(1<<i)
                    
        return x^A
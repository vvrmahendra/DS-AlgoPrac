"""Binary Strings
Problem Description
You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's. But you are allowed to perform only the following operation:
Take exactly B consecutive elements of string and change 1 to 0 and 0 to 1.
 Each operation takes 1 unit time so you have to determine the minimum time required to make the string of 1's only. If not possible return -1.  


Problem Constraints
2 ≤ length of A ≤ 1000
2 ≤ B ≤ (length of A)


Input Format
First argument is a string A consisting if 1's and 0's.
Second argument is an integer B which represents the number of consecutive elements which can be changed.


Output Format
Return an integer which is the minimum time to make the string of 1's only or -1 if not possible.


Example Input
Input 1:
 A = "00010110"
 B = 3
Input 2:
 A = "011"
 B = 3
 


Example Output
Output 1:
 3
Output 2:
 -1
 


Example Explanation
Explanation 1:
 You can get 1 by first changing the leftmost 3 elements, getting to 11110110, then the rightmost 3, getting to 11110001, 
 and finally the 3 left out 0's to 11111111; In 3 unit time.
Explanation 2:
It's not possible to convert the string into string of all 1's."""



class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    @staticmethod
    def changeBits(A, i, B):
        for i in range(i,i+B):
            if A[i] == 1: A[i] = 0
            elif A[i] == 0: A[i] = 1
    def solve(self, A, B):
        A = list(A)
        A = [int(i) for i in A]
        n = len(A)
        ans = 0
        for i in range(n-B+1):
            if A[i] == 0:
                ans += 1
                self.changeBits(A, i, B)
                
        for i in range(n-B+1, n):
            if A[i] == 0:
                return -1
                
        return ans
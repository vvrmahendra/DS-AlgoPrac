"""STRENGTH
Problem Description
Given two arrays of integers A and B of size N each and two integers C and D. Strength of two same size arrays E and F = number of corresponding elements giving sum C. Ex:- for E = [4, 6, 7] and F = [7, 6, 5] and C = 12 Strength(E, F) = 2, because E[2] + F[2] = C and E[3] + F[3] = C Return the count of pairs (E, F) such that Strength(E, F) <= D. where, E = A[i], A[i+1], ... A[j], F = B[k], B[k+1], ... B[l] and (j - i) == (l - k).     


Problem Constraints
1 <= N <= 1000
1 <= C <= 106
1 <= A[i], B[i] <= 106
1 <= D <= N


Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
The third argument given is the integer C.
The fourth argument given is the integer D.


Output Format
Return an integer denoting the count of pairs (E, F) such that Strength(E, F) <= D where, E = A[i].....A[j], F = B[k].....B[l] and (j - i) == (l -k).


Example Input
Input 1:
 A = [4, 9, 9]
 B = [2, 7, 2]
 C = 11
 D = 1
Input 2:
 A = [4, 9, 3, 7, 1]
 B = [7, 8, 4, 10, 4]
 C = 11
 D = 1
    


Example Output
Output 1:
 13
Output 2:
 50
    


Example Explanation
Explanation 1:
 Given A = [4, 9, 9], B = [2, 7, 2], C = 11
 Strength([4], [2]) = 0
 Strength([4], [7]) = 1
 Strength([4], [2]) = 0
 Strength([9], [2]) = 1
 Strength([9], [7]) = 0
 Strength([9], [2]) = 1
 Strength([9], [2]) = 1
 Strength([9], [7]) = 0
 Strength([9], [2]) = 1
 Strength([4, 9], [2, 7]) = 0
 Strength([4, 9], [7, 2]) = 2
 Strength([9, 9], [2, 7]) = 1
 Strength([9, 9], [7, 2]) = 1
 Strength([4, 9, 9], [2, 7, 2]) = 1
 13 out of 14 combinations have Strength less than or equal to 1."""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        B = [C-i for i in B]
        n = len(A)
        ans = 0
        
        for i in range(n):
            l1, r1 = 0, 0
            l2, r2 = i, i
            temp = 0
            flag = True
            while r1 < n and r2 < n:
                if flag:
                    temp += 1 if A[r1] == B[r2] else 0
                else:
                    temp -= 1 if A[l1-1] == B[l2-1] else 0
                    
                if temp <= D:
                    flag = True
                    ans += r2-l2+1
                    r1 += 1
                    r2 += 1
                else:
                    flag = False
                    l1 += 1
                    l2 += 1
                    
                    
        A, B = B, A
        
        for i in range(1,n):
            l1, r1 = 0, 0
            l2, r2 = i, i
            temp = 0
            flag = True
            while r1 < n and r2 < n:
                if flag:
                    temp += 1 if A[r1] == B[r2] else 0
                else:
                    temp -= 1 if A[l1-1] == B[l2-1] else 0
                    
                if temp <= D:
                    flag = True
                    ans += r2-l2+1
                    r1 += 1
                    r2 += 1
                else:
                    flag = False
                    l1 += 1
                    l2 += 1
        return ans
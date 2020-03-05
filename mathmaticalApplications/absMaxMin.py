"""Given an array of integers A of size N, N is even. Divide the array in two subsequences such that
1.Length of both subsequence is equal.
2.Each element of A occurs in exactly one of these subsequence.
Magic number = sum of absolute difference of corresponding elements of subsequences.
For Ex:- 
subsequence 1 = {1, 5, 1}, 
subsequence 2 = {1, 7, 11}
Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
Return an array B of size 2, where B[0] = maximum possible value of Magic number % 10^9 + 7,B[1] = minimum possible value of a Magic number % 10^9 + 7 
Input Format
The first argument given is the integer array A.
Output Format
Return an array B of size 2, where B[0] = maximum possible value of Magic number % 10^9 + 7,B[1] = minimum possible value of a Magic number % 10^9 + 7
Constraints
1 <= N <= 10^5
-10^9 <= A[i] <= 10^9
N is even
For Example
Example Input 1:
    A = [3, 11, -1, 5]
Example Output 1:
    [14, 10]
Example Explanation 1:
    All possible magical numbers:-
    sub1 = {3, 11}, sub2 = {-1, 5}, Magic Number = abs(3 - -1) + abs(11 - 5) = 10
    sub1 = {3, -1}, sub2 = {11, 5}, Magic Number = abs(3 - 11) + abs(-1 - 5) = 14
    sub1 = {3, 5}, sub2 = {11, -1}, Magic Number = abs(3 - 11) + abs(5 - -1) = 14
    sub1 = {11, -1}, sub2 = {3, 5}, Magic Number = abs(11 - 3) + abs(-1 - 5) = 14
    sub1 = {11, 5}, sub2 = {3, -1}, Magic Number = abs(11 - 3) + abs(5 - -1) = 14
    sub1 = {-1, 5}, sub2 = {3, 11}, Magic Number = abs(-1 - 3) + abs(5 - 11) = 10 
    maximum of all magic number = 14 % 10^9 + 7 = 14
    minimum of all magic number = 10 % 10^9 + 7 = 10

Input 2:
    A = [2, 2]
Output 2:
    [0, 0]
"""




def solve(self, A):
    A.sort()
    min_ = 0
    n = len(A)
    for i in range(0,n,2):
        min_ = min_ + A[i+1]-A[i]
        
    max_ = 0
    for i in range(0,n//2):
        max_ = max_ + A[n//2+i]-A[i]
    
    mod = 10**9+7    
    return [max_%mod,min_%mod]
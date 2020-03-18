"""Minimum Characters required to make a String Palindromic
Problem Description
Given a string A of size N consisting only of uppercase alphabets. 
The only operation allowed is to insert characters in the beginning of the string. 
Find and return how many minimum characters are needed to be inserted to make the string a palindrome string. 


Problem Constraints
1 <= N <= 105


Input Format
The only argument given is a string A.


Output Format
Return an integer denoting the minimum characters that are needed to be inserted to make the string a palindrome string.


Example Input
A = "ABC"


Example Output
2


Example Explanation
Insert 'B' at beginning, string becomes: "BABC".
Insert 'C' at beginning, string becomes: "CBABC"."""

#Using KMP algorithm
def solveKMP(self, A):
    def lpsTable(A):
        i, j, n = 1, 0, len(A)
        lps = [0]*n
        while i < n:
            if A[i] == A[j]:
                lps[i] = j+1
                i, j = i+1, j+1
                
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
        
    temp = A + '$' + ''.join(list(A)[::-1])
    return len(A)-lpsTable(temp)[-1]

#Using Binary Search in solution space
"""
while checking for validation there are two cases 1st with assuming even characters in string 2nd assuming odd characters
for cases like babb
for m = 2 you'll not find a solution and you'll move in right hand side without considering the case of bab
so in you else condition first check for this case just add

if mid - 1 >= 0 and isPalin(A[:chars_rem + 1]):

                    ans = mid - 1

                    right = mid - 2

 

                    continue"""
def solveBinarySearch(A):
    def isPalin(A):
        i, j = 0, len(A)-1
        while i <= j:
            if A[i] != A[j]:
                return False
            
            i, j = i+1, j-1
        return True
    
    left, right = 0, len(A)
    ans = len(A)
    while left <= right:
        mid = (left+right)//2
        chars_rem = len(A)-mid
        if isPalin(A[:chars_rem]):
            ans = mid
            right = mid-1
        else:
            if mid - 1 >= 0 and isPalin(A[:chars_rem + 1]):

                ans = mid - 1

                right = mid - 2
                continue
            left = mid+1
            
    return ans
                
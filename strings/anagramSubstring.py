"""Anagram Substring Search
Given a string A and a string B. Find and return the starting indices of the substrings of A which matches any of the anagrams of B. Note: An anagram is a play on words created by rearranging the letters of the original word to make a new word or phrase 
Input Format
The arguments given are string A and string B.
Output Format
Return the starting indices of the substrings of A which matches any of the anagrams of B.
Constraints
1 <= length of the string A,B <= 100000
length of string A > length of string B
'a' < = A[i] ,B[i] < ='z'
For Example
Input 1:
    A = "BACDGABCDA"
    B = "ABCD"
Output 1:
    [0, 5, 6]

Input 2:
    A = "AAABABAA"
    B = "AABA"
Output 2:
    [0, 1, 4]
"""


def solve(A, B):
    if len(A) < len(B):
        return []
    n , m = len(A) , len(B)
    hash_target = 0
    for i in B:
        hash_target += ord(i)**2
        
    hash_temp = 0
    for i in range(m):
        hash_temp += ord(A[i])**2
        
    ans = []
    if hash_temp == hash_target:
        ans.append(0)
    for i in range(1, n-m+1):
        hash_temp -= ord(A[i-1])**2
        hash_temp += ord(A[m+i-1])**2
        if hash_temp == hash_target:
            ans.append(i)
            
    return ans
"""Longest Common Prefix
Problem Description
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array. Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2. For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".  


Problem Constraints
0 <= sum of length of all strings <= 1000000


Input Format
The only argument given is an array of strings A.


Output Format
Return the longest common prefix of all strings in A.


Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:
A = ["abab", "ab", "abcd"];
 


Example Output
Output 1:
"a"
Output 2:
"ab"
 


Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".
Explanation 2:
Longest common prefix of all the strings is "ab".
"""



def longestCommonPrefix(A):
    if len(A) == 1:
        return A[0]
    if len(A) == 0:
        return ""
    index, flag = 0, True
    while index < len(A[0]) and flag:
        temp = A[0][index]
        for i in A[1:]:
            if (index >= len(i)) or (index  < len(i) and i[index] != temp):
                flag = False
                break
        if flag:
            index = index+1
        
    return A[0][:index]
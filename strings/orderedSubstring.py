"""Ordered Substrings
You are given an array A consisting of strings. You are supposed to order the given strings in such a way that for a particular string, all strings ordered before it exist as its substrings. Each string is made up of lowercase English letters. Return an array consisting of the correct order of strings. If it is not possible to do so, return a vector consisting of one element, which is the string "NO". Input:
A: Array of strings.
Output:
Return an array consisting of the correct order of strings. If it is not possible to do so, return a vector consisting of one element, which is the string "NO".
Constraints:
Strings in A consist of lowercase English letters
1 <= size(A) <= 100
1 <= size of strings in A <= 100
Some strings might be equal
Example:
Input:
A: [abc, abcd, a, abc]

Output:
[a, abc, abc, abcd]

Input:
A: [xyz, xz, xyzzy]

Output:
[NO]"""

def solve(A):
    def helper(A,B):
        def lpsTable(A):
            i, j, n = 0, 1, len(A)
            lps = [0]*n
            while j < n:
                if A[i] == A[j]:
                    lps[j] = i+1
                    i , j = i+1, j+1
                    
                else:
                    if i != 0:
                        i = lps[i-1]
                    else:
                        lps[j] = 0
                        j += 1
                        
            return lps
        
        n , m = len(A), len(B)
        i , j = 0, 0
        lps = lpsTable(B)
        while i < n:
            if A[i]==B[j]:
                i, j = i+1, j+1
                
            if j == m:
                return True
            elif  i < n and A[i] != B[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                
        return False
        
        
        
    A.sort(key = lambda i:len(i), reverse = True)
    for i in range(1,len(A)):
        if not helper(A[i-1],A[i]):
            # print(A[i],A[i-1])
            return ['NO']
        
    return A[::-1]
"""5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb" """

class Solution:
    @staticmethod
    def manchar(s):
        s = "#"+"#".join(list(s))+"#"
        n = len(s)
        A = [0]*n
        c, r, i = 0, 0, 0
        while i < n:
            if i < r:
                A[i] = min(A[2*c-i], r-i)
            while i+A[i]+1<n and i-A[i]-1 >=0 and s[i+A[i]+1] == s[i-A[i]-1]:
                A[i] += 1

            if i+A[i] > r:
                c = i
                r = i+A[i]
            i += 1

        return A



    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        A = self.manchar(s)
        v, m = max([(A[i], i) for i in range(len(A))])
        if v%2 == 0:
            mid = m//2
            h = v//2
            return s[mid-h:mid+h]
        else:
            mid = m//2
            h = v//2
            return s[mid-h:mid+h+1]
        
        
        
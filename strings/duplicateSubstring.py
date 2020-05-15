"""1044. Longest Duplicate Substring
Hard

235

132

Add to List

Share
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: """""


class Solution:
    def isexist(self, A, mid, b, mod, n):
        seen = set()
        encode = 0
        for i in range(mid):
            encode = (encode*b+A[i])%mod
            
        seen.add(encode)
        use = (b**(mid))%mod
        for i in range(1,n-mid+1):
            encode = (encode*b-A[i-1]*use+A[i+mid-1])%mod
            if encode in seen:
                return i
            seen.add(encode)
            
        return -1
            
    def longestDupSubstring(self, S: str) -> str:
        
        nums = [ord(i)-ord('a') for i in S]
        n, modulus,a = len(S), 2**32, 26
        
        
        ans = ""
        left, right = 1, n-1
        while left <= right:
            L = (right + left) // 2
            temp = self.isexist(nums, L, a, modulus, n)
            if temp != -1:
                ans = S[temp:temp+L]
                left = L + 1
            else:
                right = L - 1
               
        
        return ans
                
                
        
        
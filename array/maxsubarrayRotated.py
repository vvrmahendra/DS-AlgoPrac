"""918. Maximum Sum Circular Subarray
Medium

589

26

Add to List

Share
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)"""

class Solution:
    def getminsum(self, A):
        ans = 0
        minTill = 0
        for i in A:
            minTill += i
            if minTill > 0:
                minTill = 0
            ans = min(ans, minTill)
            
        return ans
    
    def getmaxsum(self,A):
        ans = 0
        maxtill = 0
        for i in A:
            maxtill += i
            if maxtill < 0:
                maxtill = 0
                
            ans = max(ans, maxtill)
            
        return ans
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if max(A) <= 0: return max(A)
        if min(A) >= 0: return sum(A)
        
        min_ = self.getminsum(A)
        max_ = self.getmaxsum(A)
        return max(sum(A)-min_, max_)
        
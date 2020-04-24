"""Another GCD problem
Problem Description
Given an integer array A of size N. Find the maximum length of a subarray Al, Al+1 ... Ar such that gcd(A[l], A[l+1], ... A[r]) > 1. NOTE: If no such subarray exists, return -1.    


Problem Constraints
1 <= N <= 105
0 <= A[i] <= 106


Input Format
First and only argument is an integer array A of size N.


Output Format
Return an integer denoting the maximum length of a subarray.


Example Input
Input 1:
 A = [7, 1, 2, 3, 4]
Input 2:
 A = [2, 4, 6, 8, 20]
    


Example Output
Output 1:
 1
Output 2:
 5
    


Example Explanation
Explanation 1:
 Gcd of every two consecutive element is 1. So, we can not take more than 1 element in any subarray. So, the answer is 1.
Explanation 2:
 Gcd of all elements in the array is greater than 1 which is 2. So, the maximum length of the subarray is 5."""


class Solution:
    # @param A : list of integers
    # @return an integer
    def _prime(self, n):
        prime = [i for i in range(n+1)]
        prime[1] = 0
        sqN = int(n**0.5)
        for i in range(2,sqN+1):
            if prime[i] == i:
                j = i*i
                while j <= n:
                    if prime[j] == j:
                        prime[j] = i
                    j += i
                    
        return prime
        
    def solve(self, A):
        primes = self._prime(max(A))
        n = len(A)
        from collections import defaultdict
        dict_ = defaultdict(list)
        for i, val in enumerate(A):
            while val>=2:
                lpm = primes[val]
                dict_[lpm].append(i)
                while val%lpm == 0:
                    val = val//lpm
                
        # print(dict_)        
        ans = -1
        for ele in dict_:
            tempans = -1
            i, j = 0, 1
            while j < len(dict_[ele]):
                if dict_[ele][j] == dict_[ele][j-1]+1:
                    j += 1
                else:
                    # print(j,i)
                    tempans = max(tempans, j-i)
                    i = j
                    j += 1
                    
            tempans = max(tempans, j-i)
                    
            ans = max(ans, tempans)
            
        return ans

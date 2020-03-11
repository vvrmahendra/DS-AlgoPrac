"""Count Subarrays
Problem Description
Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements. Since the number of subarrays could be large, return value % 109 +7. 


Problem Constraints
1 <= N <= 105 1 <= A[i] <= 106  


Input Format
The only argument given is an Array A, having N integers.


Output Format
Return the number of subarrays of A, that have unique elements.


Example Input
A = [1, 1, 3]


Example Output
4


Example Explanation
Subarrays of A that have unique elements only:
[1], [1], [1, 3], [3]
"""


def solve(A):
    def helper(a,b):
        first = a*(a+1)//2
        second = b*(b+1)//2
        return first-second
            
    if len(A) <= 1:
        return len(A)
        
    dict_ = {}
    n = len(A)
    ans, i, index_, j = 0, 0, 0, 1

    dict_[A[0]] = 0
    while j < n:
        if A[j] not in dict_:
            dict_[A[j]] = j
            j += 1
            
        elif dict_[A[j]] < index_:
            dict_[A[j]] = j
            j += 1
            
        else:
            ans += helper(j-index_,i-index_)
            index_ = dict_[A[j]]+1
            dict_[A[j]] = j
            i = j
            j += 1
            
        
    ans += helper(j-index_,i-index_)
    return ans%(10**9+7)

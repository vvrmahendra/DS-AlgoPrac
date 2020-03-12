"""Sort an array according to the order defined by another array
Given two array of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B. For the elements not present in B, append them at last in sorted order. Return the array A after sorting from the above method. Note: Elements of B are unique. 
Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
Output Format
Return the array A after sorting as described.
Constraints
1 <= length of the array A <= 100000
1 <= length of the array B <= 100000
-10^9 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = [5, 4, 2]
Output 1:
    A = [5, 4, 2, 1, 3]

Input 2:
    A = [5, 17, 100, 11]
    B = [1, 100]
Output 2:
    [100, 5, 11, 17]
"""




def solve(self, A, B):
    n, min_, len_, dict_ = len(A), min(A), 0, {}
    for i in B:
        dict_[i] = 0
        
    for i in range(n):
        if A[i] in dict_:
            len_ += 1
            dict_[A[i]] += 1
            A[i] = min_
    
    A.sort()
    index, i = 0, 0
    while i < len_:
        while dict_[B[index]] > 0:
            A[i] = B[index]
            dict_[B[index]] -= 1
            i += 1
            
        index += 1
        
    return A
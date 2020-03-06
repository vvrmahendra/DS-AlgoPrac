"""Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array. What is the most number of chunks we could have made? 
Input Format
The only argument given is the integer array A.
Output Format
Return the maximum number of chunks that we could have made.
Constraints
1 <= N <= 100000
0 <= A[i] < N 
For Example
Input 1:
    A = [1, 2, 3, 4, 0]
Output 1:
    1

Input 2:
    A = [2, 0, 1, 3]
Output 2:
    2"""


def solve(A):
    ans = 0
    pre_A  = [None]*len(A)
    pre_A[0] = A[0]
    for i in range(1,len(A)):
        pre_A[i] = max(pre_A[i-1],A[i])
    print(pre_A)
    for index,value in enumerate(pre_A):
        print(index,value)
        if index == value:
            ans += 1
            
    return ans

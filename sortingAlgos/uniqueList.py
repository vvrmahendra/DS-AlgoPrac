"""Unique Elements
You are given an array A of N elements. You have to make all elements unique, to do so in one step you can increase any number by one. Find the minimum number of steps.
 Input Format
The only argument given is an Array A, having N integers.
Output Format
Return the Minimum number of steps required to make all elements unique.
Constraints
1 <= N <= 1e4
1 <= A[i] <= N
For Example
Example Input:
    A = [1, 1, 3]
Example Output: 1
Explanation:
    we can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3]"""

"""
I have solved it in both recursive way and iterative way.
Iterative way is trickier.
"""



def solveRecursive( A):
    if len(A) <= 0:
        return 0
    A.sort()
    import sys
    sys.setrecursionlimit(100000)
    def approach(A,index,ans):
        n = len(A)
        if index == n:
            return ans
        
        if A[index] <= A[index-1]:
            ans += A[index-1]-A[index]+1
            A[index] = A[index-1]+1
            
        ans = approach(A,index+1,ans)
        return ans
        
    return approach(A,1,0)

def solveIterative( A):
    if len(A) <= 0:
        return 0
    A.sort()
    n = len(A)
    i = 1
    j = 0
    ans = 0
    while j < n:
        if i >= A[j]:
            ans += i-A[j]
            j += 1
            
        i += 1
        
    return ans
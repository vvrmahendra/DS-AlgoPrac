"""Order them
Given an array of integers A describing ranking of trucks. Your task is to insert these rank in another array B by some means of operations such that B is sorted in ascending order. For performing these operations you can use one stack C. In one Operation you can perform any of the following steps:
Remove the first element from A and append at the back of C.
Remove the last element from C and append at the back of B.
Remove the first element from A and append at the back of B.
you can perform these operations any number of times (possibly zero). Return 1 if B can be formed in ascending order using some operations else return 0. 
Input Format
The only argument given is the integer array A.
Output Format
   Return 1 if B can be formed in ascending order using some operations else return 0.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= length of Array
All elements of A are distinct.
For Example
Input 1:
    A = [5, 1, 2, 4, 3]
Output 1:
    1
    step 1: A = [5, 1, 2, 4, 3]
            B = []
            C = []
    step 2: A = [1, 2, 4, 3]
            B = [5]
            C = []
    step 3: A = [2, 4, 3]
            B = [5]
            C = [1]
    step 4: A = [4, 3]
            B = [5]
            C = [1, 2]
    step 5: A = [3]
            B = [5, 4]
            C = [1, 2]
    step 6: A = []
            B = [5, 4]
            C = [1, 2, 3]
    step 7: A = []
            B = [5]
            C = [1, 2, 3, 4]
    step 8: A = []
            B = []
            C = [1, 2, 3, 4, 5]



Input 2:
    A = [5, 3, 1, 4, 2]
Output 2:
    0
"""

def solve(A):
    B, C =[], [] 
    i, n, = 0, len(A)
    while i < n:
        if B:
            while C and C[-1] == B[-1]+1:
                B.append(C.pop())
            
            while i < n and A[i] != B[-1]+1:
                C.append(A[i])
                i += 1
                
            if i < n and A[i] == B[-1]+1:
                B.append(A[i])
            else:
                return 0
                    
        else:
            while A[i] != 1:
                C.append(A[i])
                i += 1
                
            B.append(A[i])
            
        i += 1
        
    while C and C[-1] == B[-1]+1:
        B.append(C.pop())
        
    if len(B) == n:
        return 1
    else:
        return 0
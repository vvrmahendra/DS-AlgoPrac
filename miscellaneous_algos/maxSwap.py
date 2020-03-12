"""Swap elements
Problem Description
Given an integer array A of size N. In the array, you can swap (A[i],A[j]) if the following conditions are satisfied:
i < j
i is a divisor of j
You are also provided M independent queries. In each query, you are given two integers idx and K. For each query, you are required to output the maximum number you can retrieve at index idx after performing at most K swaps. NOTE 1: Queries are given by a 2-D integer array B of size M * 2 where B[i][0] denotes idx and B[i][1] denotes K. NOTE 2: Consider array A as 1-based indexed.      


Problem Constraints
1 <= N,M <= 50000
1 <= A[i] <= 109
1 <= B[i][0] <= N
0 <= B[i][1] <= 100


Input Format
First argument is an integer array A of size N.
Second argument is a 2-D integer array B of size M.


Output Format
Return an integer array of size M denoting output for each query as decribed above.


Example Input
A=[2,4,6,3,2]
B=[ [5,1]
    [4,1]
    [4,0] ]


Example Output
[2,4,3]


Example Explanation
For first query idx=5 and K=1. You can only swap element which is at index 1 (since 1 is the only divisor of 5 less than 5).
For second query idx=4 and K=1. You can swap element which is at index 1 or 2 (since 1 and 2 are the divisor of 4 less than 4).
For third query idx=4 and K=0. You cannot swap any element since K=0.
"""



def solve(A, B):
    A = [0]+A
    n = len(A)
    ans = []
    max_a = max(A)
                
    for query in B:
        if query[1] == 0:
            ans.append(A[query[0]])
            
        elif query[1] > 1:
            ans.append(max_a)
            
        else:
            temp = A[query[0]]
            for i in range(1,int(query[0]**0.5)+1):
                if query[0]%i == 0:
                    temp = max(temp,A[i])
                    temp = max(temp,A[query[0]//i])
                
            j = 2*query[0]
            while j < n:
                temp = max(temp, A[j])
                j += query[0]
                
            ans.append(temp)
            
    return ans
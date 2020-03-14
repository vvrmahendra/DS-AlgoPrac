"""Compare Sorted Subarrays
Given an array A of length N. You have to answer Q queires. Each query will contain 4 integers l1, r1, l2 and r2. If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.
NOTE - The queries are 0-indexed.
Input:
1st will be array A. 2nd will be 2-D array denoting queries with dimension Q * 4. 
Consider ith query as Arr[i][0], Arr[i][1], Arr[i][2] and Arr[i][3]. 
Output:
Return an array of length Q with answer of the queries in the same order in input. 
Constraint:
0 <= A[i] <= 100000
1 <= N <= 100000
1 <= Q <= 100000
Example:
Input:
A = [1 7 11 8 11 7 1]
Q = [[0 2 4 6]] 

Output:
[1]

Explanation:
(0, 2) -> [1 7 11]
(4, 6) -> [11 7 1]
Both are same when sorted hence 1.
"""


def solve(A, B):
    n = len(A)
    hash_A = [A[i]*A[i] for i in range(n)]
    pre_A, pre_hash = [0]*(n+1), [0]*(n+1)
    pre_A[0] = A[0]
    pre_hash[0] = hash_A[0]
    for i in range(1,n):
        pre_A[i] = pre_A[i-1]+A[i]
        pre_hash[i] = pre_hash[i-1]+hash_A[i]
        
    ans = []
    for Q in B:
        i, j, k, l = Q
        if pre_A[j]-pre_A[i-1] == pre_A[l]-pre_A[k-1]:
            if pre_hash[j]-pre_hash[i-1] == pre_hash[l]-pre_hash[k-1]:
                ans.append(1)
            else:
                ans.append(0)
        else:
            ans.append(0)
            
    return ans
"""Maximum Frequency stack
You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it. Operations are of two types:
1 x: push an integer x onto the stack and return -1
2 0: remove and return the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.
A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed. 
Input Format
The only argument given is the integer array A.
Output Format
Return the array of integers denoting answer to each operation.
Constraints
1 <= N <= 100000
1 <= A[i][0] <= 2
0 <= A[i][1] <= 10^9
For Example
Input 1:
    A = A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Output 1:
    [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]

Input 2:
    A = A = [   
            [1, 5]
            [2 0]
            [1 4]   ]
Output 2:
    [-1, 5, -1]"""

def solve(A):
    from collections import defaultdict
    dict_ = defaultdict(int)
    ans = []
    set_ = defaultdict(list)
    max_freq = 0
    for Q in A:
        if Q[0] == 1:
            dict_[Q[1]] += 1
            max_freq = max(max_freq, dict_[Q[1]])
            set_[dict_[Q[1]]].append(Q[1])
            ans.append(-1)
        else:
            
            element = set_[max_freq].pop()
            max_freq = max_freq if set_[max_freq] else max_freq-1
            ans.append(element)
            dict_[element] -= 1
            
    return ans
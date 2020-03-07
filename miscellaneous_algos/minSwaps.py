"""Minimum Swaps 2
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)]. It is allowed to swap any two elements (not necessarily consecutive). Find the minimum number of swaps required to sort the array in ascending order. 
Input Format
The only argument given is the integer array A.
Output Format
Return the minimum number of swaps.
Constraints
1 <= N <= 100000
0 <= A[i] < N
For Example
Example Input 1:
    A = [1, 2, 3, 4, 0]
Example Output 1:
    4
Explanation:
    You cannot sort it with lesser swaps
Example Input 2:
    A = [2, 0, 1, 3]
Example Output 2:
    2"""


def solve(A):
    
    # Arr = sorted(A)
    dict_ = {}
    for i in range(len(A)):
        dict_[A[i]] = i
        
    ans = 0
    while len(dict_) > 0:
        cycle = 0
        # first = list(dict_.keys())[0]
        first,temp = dict_.popitem()
        dict_[first] = temp
        #dict_.pop(first)
        # print(len(dict_))
        while True:
            if first in dict_:
                next_ = dict_[first]
                cycle += 1
                dict_.pop(first)
                first = next_
            else:
                break
        ans += cycle-1
        
    return ans
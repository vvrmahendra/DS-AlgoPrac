"""Sort the permutation
Problem Description
Given a permutation of size N. Each number has some color associated to it.
Find the maximum number of colors that can be used such that you are able to sort the permutation by swapping the elements having same color.


Problem Constraints
1 <= N <= 100000


Input Format
First argument is an array of size N consisting of all elements from 1 to N.


Output Format
Return an integer denoting the maximum number of colors that can be used.


Example Input
Input 1:
A = [1,4,2,3]


Example Output
Output 1:
2


Example Explanation
Explanation 1:
We can color 4, 2, 3 with same color and 1 with different color.
Given A = [1,4,2,3].
After swapping 4 and 2,  A => [1,2,4,3].
Now swap 4 and 3 to get the sorted permutation A => [1,2,3,4].
"""


"""
Main motto is to divide them into non overlaping cycles.
"""




def solve(A):
    ans = 0
    n = len(A)
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            ans += 1
            j = i
            while not visited[j]:
                visited[j] = 1
                j = A[j-1]
                
    return ans
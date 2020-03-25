"""Hire candidates
Problem Description
A company wants to hire maximum number of students from a college. The company cannot spend more than A amount to hire students. There are N students numbered 1 to N and the base cost to hire students is given by an integer array B of size N. The final cost of students depends on the number of students the company hire.
If a company hires X students then the final cost to hire the ith student will be B[i] + (i*X) (where i is the number of that student). Find the maximum value of X and the minimum cost to hire X people. NOTE: Cost to hire students X should be less than equal to A.    


Problem Constraints
1 <= N <= 100000 1 <= A, B[i] <= 109   


Input Format
First argument is an integer A.
Second argument is an integer array B.


Output Format
Return an integer array of size 2, first element denoting maximum value of X and second element denoting the minimum cost to hire X students.


Example Input
 A = 20
 B = [9, 4, 2, 3,  2]


Example Output
 [2, 16]


Example Explanation
 We can select maximum of 2 students then the final cost of each student will be [11, 8, 8, 11, 12].
 For student 1: 9 + 1 * 2 = 11
 For student 2: 4 + 2 * 2 = 8
 For student 3: 2 + 3 * 2 = 8
 For student 4: 3 + 4 * 2 = 11
 For student 5: 2 + 5 * 2 = 12
 So, the minimum cost of selecting two students will be 16.
"""


def solve(A, B):
    def helper(A, val, target):
        B = [A[i]+(i+1)*val for i in range(len(A))]
        B.sort()
        return [True,sum(B[:val])] if sum(B[:val]) <= target else [False, -1]
        
    left, right = 0, A
    ans = [None, None]
    while left <= right:
        mid = (left+right)//2
        temp = helper(B, mid, A)
        if temp[0]:
            ans = [mid,temp[1] ]
            left = mid+1
        else:
            right = mid-1
            
    return ans
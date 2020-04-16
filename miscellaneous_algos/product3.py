"""Product of 3
You are given an array A that has N integers. You have to find the product of the 3 largest integers in array A from range 1 to i, where i goes from 1 to N. Return an array where the integer at index i of the array is the product of the largest 3 integers in range 1 to i in array A. If i<3, then the integer at index i is -1. Input Format
A: Array of integers
Output Format
Return an array where the integer at index i of the array is the product of the largest 3 integers in range 1 to i in array A. If i<3, then the integer at index i is -1.
Constraints:
1 <= size(A) <= 10^5
0 <= Integers in A <= 10^3
Example Input
A: [1, 2, 3, 4, 5]
Example Output
[-1, -1, 6, 24, 60]
Explanation For i=1, i<3 so ans[i] = -1. For i=2, i<3 so ans[i] = -1. For i=3, ans[i] = 123 = 6. For i=4, ans[i] = 432 = 24. For i=5, ans[i] = 543 = 60."""

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def solve(self, A):
        if len(A) <=2 : return [-1 for i in A]
        min_ = []
        max_ = []
        ans = []
        for i in A:
            if len(ans) < 2:
                min_.append(i)
                max_.append(i)
                ans.append(-1)
            else:
                max_.append(i)
                max_.sort(reverse = True)
                a, b, c = max_[:3]
                if len(max_) > 3:
                    max_.pop()
                min_.append(i)
                min_.sort()
                min_.pop()
                d, e = min_
                ans.append(max(a*b*c, a*d*e))
        return ans
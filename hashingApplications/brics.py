"""Cross the wall
Problem Description
There is a rectangular brick wall consisting of several rows of bricks.
The wall has A rows and length of each row is B units. The bricks have the same height that can be considered as 1 unit but has different length. You are given an integer array C denoting length of N bricks.
The bricks are chosen one by one from the left of the array and each row of the wall is build from left to right.
While building the wall, if the sum of length of bricks in a row is equal to B then start building another row again from left to right. Input is such that, you will end up building the wall consisiting of A rows and length of each row will be equal to B. You need to find a vertical line going from top to bottom of the wall that crossed through the fewest number of bricks.
Return the least number of bricks through which the vertical line crossed. NOTE: 
If your line go through the edge of a brick, then the brick is not considered as crossed.
You cannot draw a vertical line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
   


Problem Constraints
1 <= N <= 105 1 <= A x B <= 109 1 <= C[i] <= 109   


Input Format
First argument is an integer A denoting the height of the wall.
Second argument is an integer B denoting the length of the wall.
Third argument is an integer array C of size N denoting length of bricks.


Output Format
Return an integer denoting the minimum number of crossed bricks.


Example Input
Input 1:
 A = 2
 B = 7
 C = [3, 4, 2 ,2, 3]
Input 2:
 A = 3
 B = 5
 C = [1, 2, 2, 5, 3, 2]
  


Example Output
Output 1:
 1
Output 2:
 1
  


Example Explanation
Explanation 1:
 We can create a line at length 2 of the wall. So, the line will cross only 1 brick at height 1.
Explanation 2:
 We can create a line at length 3 of the wall. So, the line will cross only 1 brick at height 2."""

from collections import defaultdict
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        dict_ = defaultdict(int)
        i = 0
        while i < len(C):
            sum_ = 0
            while sum_ < B:
                if 0 < sum_ < B:
                    dict_[sum_] += 1
                
                sum_ += C[i]
                i += 1
                
        ans = A
        for i in dict_:
            ans = min(ans, A-dict_[i])
            
        return ans
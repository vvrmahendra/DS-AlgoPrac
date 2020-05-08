"""Sweet dish
Problem Description
Akash has N ingredients and ith ingredients have Ai sweetness. He wants to make a perfect dish using some given ingredients. A dish will be perfect if it has following properties
There is at least one ingredient in the dish whose sweetness value is a prime number.
The total sweetness of the dish must be at least B and at most C.
 Find the number of ways to make the perfect dish.       


Problem Constraints
1 <= N <= 18
2 <= A[i] <= 109
2 <= B <= C <= 109


Input Format
First argument is an integer array A denoting the sweetness of the ingredients.
Second argument is an integer B.
Third argument is an integer C.


Output Format
Return an integer denoting the number of ways to make the perfect dish.


Example Input
Input 1:
 A = [2, 2, 4, 5]
 B = 3
 C = 7
 Input 2:
 A = [1, 3, 7, 4]
 B = 5
 C = 8
  


Example Output
Output 1:
 6
 Output 2:
 5
  


Example Explanation
Explanation 1:
 There are 6 ways to make dish using the given ingredients: [2, 2], [2, 4], [2, 4], [2, 5], [2, 5], [5].
  Explanation 2:
 There are 5 ways to make dish using the given ingredients: [3, 4], [1, 4], [1, 7], [1, 3, 4], [3, 4].
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    @staticmethod
    def isPrime(A):
        if A <= 2: return True
        sqA = int(A**0.5)+1
        for i in range(2,sqA):
            if A%i == 0:
                return False
                
        return True
    def solve(self, A, B, C):
        p = [1 if self.isPrime(i) else 0 for i in A]
        ans = 0
        n = len(A)
        for i in range(2**n):
            sum_ = 0
            flag = False
            t = 0
            while (1 << t) <= i:
                sum_ += A[t] if (1<<t & i) else 0
                flag = flag or (bool(p[t]) if (1 << t & i) else False)
                t += 1
            if flag and B <= sum_ <=C:
                ans += 1
                
        return ans
            
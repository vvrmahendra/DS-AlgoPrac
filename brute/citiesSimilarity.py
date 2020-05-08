"""Similarity Between Cities!
Problem Description
You are given a 2-D array A of size N x 2 denoting the list of ( city, visitor ) pairs that represents visitors visiting cities. Come up with a program that identifies the pair of two different cities with the greatest similarity. The similarity metric between two different cities x, y is defined as:        
Let a be the count of common visitors among x, y.
Let b be the total of number of distinct visitors among x,y i.e union of visitors of city x and city y.
Then Similarity(x, y) = a / b where ('/' implies division operator).
 NOTE:      
If suppose two pair of cities (a, b) and (c, d) has same similarity then more priority will be given to the pair which is lexographical. smaller one.
A pair (a, b) is lexographical smaller than pair (c, d) if a < c or if a == c then b < d
       


Problem Constraints
2 <= N <= 10000
1 <= Number of Distinct Cities <= 1000
1 <= Total Number of visitors <= 10
Max Number of visitors to any city is at-most 10.
Each ( city, visitor ) pair occurs at-most one times in the input.
It is assumed that answer always exists.


Input Format
First and only argument is and two-dimensional array named A in which each row represents a pair. A[i][0] represent city and A[i][1] represent student. A[i][0]>=1 && A[i][0]<=1000 && A[i][1]>=1 && A[i][1]<=10      


Output Format
Return a one-dimensional array of size 2 in which first and second elements represents two distinct cities that forms a pair with highest similarity. NOTE:     The array you return must be sorted in non-decreasing order. As Similarity(a, b) = Similarity(b, a).       


Example Input
Input 1:
 A = [ [1, 2],
       [1, 3],
       [1, 5],
       [2, 2],
       [2, 6],
       [2, 9],
       [3, 2],
       [3, 3],
       [3, 5] ]
Input 2:
 A = [ [5, 1],
       [5, 2],
       [2, 1],
       [2, 2],
       [1, 1],
       [1, 2] ]
     


Example Output
Output 1:
 [1, 3]
Output 2:
 [1, 2]
     


Example Explanation
Explanation 1:
 Pair [1, 2] represents that visitor number 2 visits city number 1.
    Similarity(1, 2) = 0/6 = 0 as they have no visitors in common.
    Similarity(1, 3) = 3/3 = 1 as they have 3 visitors in common and total number of distinct visitors(union) among city 1 and city 3 is 3.
    Similarity(2, 3) = 1/5 = 0.2.
So city 1 and city 3 are the best pairs we can have.
Explanation 2:
 Pair [1, 2], [2, 5], [1, 5] all have same similarity scores but [1, 5] is lexographically smaller than [2, 5] so it will be given more
 prioirty but [1, 2] is lexographically smaller than [1, 5] and [2, 5] so [1, 2] will be the output.
 The answer can be even [2, 1] as Similarity(1, 2) = Similarity(2, 1) but you need to answer in non-decreasing order so output will be [1, 2]."""

from collections import defaultdict
from fractions import Fraction
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        dict_ = defaultdict(set)
        for c, v in A:
            dict_[c].add(v)
            
        C = list(dict_.keys())
        n = len(C)
        ans = [float("inf"), float("inf")]
        ansFra = Fraction(0)
        for i in range(n-1):
            for j in range(i+1,n):
                common = len(dict_[C[i]].intersection(dict_[C[j]]))
                all = len(dict_[C[i]].union(dict_[C[j]]))
                if all != 0:
                    cur = Fraction(common, all)
                    if cur > ansFra:
                        ansFra = cur
                        ans = [C[i], C[j]] if C[i] <= C[j] else [C[j], C[i]]
                    elif cur == ansFra:
                        temp = [C[i], C[j]] if C[i] <= C[j] else [C[j], C[i]]
                        if temp < ans:
                            ans = temp
                            
        return ans
                        
        
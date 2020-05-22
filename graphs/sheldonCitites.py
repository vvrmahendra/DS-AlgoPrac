"""Sheldon and Pair of Cities
Problem Description
Sheldon lives in a country with A cities (numbered from 1 to A) and B bidirectional roads. Roads are denoted by integer array D, E and F of size M, where D[i] and E[i] denotes the cities and F[i] denotes the distance between the cities. Now he has many lectures to give in the city and is running short of time, so he asked you C queries, for each query i, find the shortest distance between city G[i] and H[i]. If the two cities are not connected then the distance between them is assumed to be -1. 


Problem Constraints
1 <= A <= 200 1 <= B <= 200000 1 <= C <= 100000 1 <= F[i] <= 1000000 1 <= D[i], E[i], G[i], H[i] <= A 


Input Format
First argument is an integer A.
Seocnd argument is an integer B.
Third argument is an integer C.
Fourth argument is an integer array D.
Fifth argument is an integer array E.
Sixth argument is an integer array F.
Seventh argument is an integer array G.
Eight argument is an integer array H.


Output Format
Return an integer array of size C, for each query denoting the shortest distance between the given two vertices.
If the two vertices are not connected then output -1.


Example Input
Input 1:
 A = 4
 B = 6
 C = 2
 D = [1, 2, 3, 2, 4, 3]
 E = [2, 3, 4, 4, 1, 1]
 F = [4, 1, 1, 1, 1, 1]
 G = [1, 1]
 H = [2, 3]
Input 2:
 A = 3
 B = 3
 C = 2
 D = [1, 2, 1]
 E = [2, 3, 3]
 F = [3, 1, 1]
 G = [2, 1]
 H = [3, 2]


Example Output
Output 1:
 [2, 1]
Output 2:
 [1, 2]


Example Explanation
Explanation 1:
 Distance between (1,2) will 2 if we take path 1->4->2.
 Distance between (1,3) will 1 if we take path 1->3.
Explanation 2:
 Distance between (2,3) will 1 if we take path 1->3.
 Distance between (1,2) will 2 if we take path 1->3->2."""



 from collections import defaultdict
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : list of integers
	# @param E : list of integers
	# @param F : list of integers
	# @param G : list of integers
	# @param H : list of integers
	# @return a list of integers
	def solve(self, A, B, C, D, E, F, G, H):
        dp = [[float('inf')] * (A+1) for _ in range(A+1)]
        
        for p,c,w in zip(D,E,F):
            dp[p][c] = min(dp[p][c],w)
            dp[c][p] = min(dp[c][p],w)
                
        for i in range(1,A+1):
            dp[i][i] = 0
            
        for k in range(1,A+1):
            for i in range(1,A+1):
                for j in range(1,A+1):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
                    
        return [dp[i][j] if dp[i][j] != float('inf') else -1 for i,j in zip(G,H)]
                
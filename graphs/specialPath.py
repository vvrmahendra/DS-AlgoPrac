"""Special path
Problem Description
Given a graph with N nodes numbered 1 to N and M weighted edges. Given a binary array A of size N. A[i] = 1 if the ith node is special else 0. Find the minimum distance of the special path between the 1st and the Nth node. Distance between two nodes is defined as the sum of the weight of edges in the path. A special path is a path which visits alteast C non-special nodes and atleast D special nodes. NOTE: A node or edge can occur multiple times in a special path. If no such path exists return -1.              


Problem Constraints
1 <= N, M <= 10000
0 <= A[i] <= 1
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 100000
0 <= C, D <= 10


Input Format
First argument is an integer array A of size N
Second argument is a 2-D integer array B of size M*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]
Third argument is an integer C
Fourth argument is an integer D


Output Format
Return an integer denoting the minimum distance of the special path. Return -1 if no such path exists.


Example Input
Input 1:
A = [0, 1, 0]
B = [ [1, 2, 3], [2, 3, 5] ] 
C = 2
D = 3
  Input 2:            
A = [1, 1]
B = [ [1, 2, 1] ]
C = 1
D = 1
       


Example Output
Output 1:
 20
   Output 2:            
 -1
       


Example Explanation
Explanation 1:
 Minimum distance of the special path is 20 ( 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 3).
 Number of visits of non-special nodes = 4 (1, 1, 1, 3)
 Number of visits of special nodes = 3 (2, 2, 2)
   Explanation 2:            
 Cannot be achieved."""


from heapq import *
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        A = [0]+A
        rays, dp = defaultdict(list), defaultdict(lambda:float('inf'))

        for p,c, w in B:
            rays[p].append((c,w))
            rays[c].append((p,w))
            
        if A[1] == 1:
            dp[(1,0,1)] = 0
            heap = [(0,1,0,1)]
        else:
            dp[(1,1,0)] = 0
            heap = [(0,1,1,0)]
            
        while heap:
            w, cur, e1, e2 = heappop(heap)
            if e1 >= C and e2 >= D and cur == len(A)-1:
                return w
                
            if dp[(cur, e1, e2)] < w:
                continue
            
            
            for nei, tw in rays[cur]:
                if A[nei] == 0:
                    dp[(nei, min(e1+1,C), e2)] = min(dp[(nei, min(e1+1,C), e2)], w+tw)
                    heappush(heap, (w+tw, nei, min(e1+1,C), e2))
                else:
                    dp[(nei, e1, min(e2+1,D))] = min(dp[(nei, e1, min(e2+1,D))], w+tw)
                    heappush(heap, (w+tw, nei,  e1, min(e2+1,D)))
                
        return -1

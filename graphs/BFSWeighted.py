"""Another BFS
Problem Description
Given a weighted undirected graph having A nodes, a source node C and destination node D. Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1. You are expected to do it in Time Complexity of O(A + M). Note: There are no self-loops in the graph. No multiple edges between two pair of vertices. The graph may or may not be connected. Nodes are Numbered from 0 to A-1. Your solution will run on multiple testcases. If you are using global variables make sure to clear them.     


Problem Constraints
1 <= A <= 105 0 <= B[i][0], B[i][1] < A 1 <= B[i][2] <= 2 0 <= C < A 0 <= D < A     


Input Format
The first argument given is an integer A, representing the number of nodes. The second argument given is the matrix B, where B[i][0] and B[i][1] are connected through an edge of weight B[i][2]. The third argument given is an integer C, representing the source node. The fourth argument is an integer D, representing the destination node. Note: B[i][2] will be either 1 or 2.     


Output Format
Return the shortest distance from C to D. If it is impossible to reach node D from C then return -1.


Example Input
Input 1:
 
A = 6
B = [   [2, 5, 1]
        [1, 3, 1] 
        [0, 5, 2] 
        [0, 2, 2] 
        [1, 4, 1] 
        [0, 1, 1] ] 
C = 3
D = 2
  Input 2:            
A = 2
B = [   [0, 1, 1]
    ] 
C = 0
D = 1
       


Example Output
Output 1:
 4
  Output 2:            
 1
       


Example Explanation
Explanation 1:
The path to be followed will be:
    3 -> 1 (Edge weight : 1)
    1 -> 0 (Edge weight : 1)
    0 -> 2 (Edge weight : 2)
Total length of path = 1 + 1 + 2 = 4.
  Explanation 2:            
 Path will be 0-> 1."""


 from collections import defaultdict, deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        flag = A
        rays = defaultdict(list)
        for p, c, w in B:
            if w == 1:
                rays[p].append(c)
                rays[c].append(p)
            else:
                rays[p].append(flag)
                rays[flag].append(p)
                rays[flag].append(c)
                rays[c].append(flag)
                flag += 1
                
        visited = set()
        q = deque()
        q.append((C,0))
        while q:
            cur, dep = q.popleft()
            if cur == D:
                return dep
            visited.add(cur)
            for nei in rays[cur]:
                if nei not in visited:
                    q.append((nei, dep+1))
                    
        return -1
                
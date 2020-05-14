"""First Depth First Search
Problem Description
You are given n towns (1 to n). All towns are connected via unique directed path as mentioned in the input. Given 2 towns find whether you can reach the first town from the second without repeating any edge. x y : query to find whether x is reachable from y. Input contains an integer array A of size n and 2 integers x and y ( 1 <= x, y <= n ). There exist a directed edge from A[i] to i+1 for every 1 <= i < n. Also, it's guaranteed that A[i] <= i.    


Problem Constraints
1 <= n <= 100000


Input Format
First argument is vector A Second argument is integer B   First argument is integer C   


Output Format
Return 1 if reachable, 0 otherwise.


Example Input
Input 1:        
 A = [1, 2]B = 1C = 2
  Input 2:          
 A = [1, 2]B = 2C = 1
      


Example Output
Output 1:
 0
  Output 2:          
 1
      


Example Explanation
Explanation 1:
 Tree is 1--> 2 and hence 1 is not reachable from 2.
  Explanation 2:          
 Tree is 1--> 2 and hence 2 is reachable from 1."""



 from collections import defaultdict, deque
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, A, B, C):
        rays = defaultdict(list)
        for i, val in enumerate(A):
            rays[val].append(i+1)
            
        visited = set()
        q = deque()
        q.append(C)
        while q:
            cur = q.popleft()
            visited.add(cur)
            if cur == B:
                return 1
                
            for nei in rays[cur]:
                if nei not in visited:
                    q.append(nei)
        return 0
            
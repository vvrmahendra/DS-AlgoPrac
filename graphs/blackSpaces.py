"""Black Shapes
Problem Description
Given character matrix A of O's and X's, where O = white, X = black. Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)      


Problem Constraints
1 <= |A|,|A[0]| <= 1000 A[i][j] = 'X' or 'O'      


Input Format
The First and only argument is character matrix A.


Output Format
Return a single integer denoting number of black shapes.


Example Input
Input 1:
A = [ [X, X, X], [X, X, X], [X, X, X] ]
  Input 2:              
A = [ [X, O], [O, X] ]
        


Example Output
Output 1:
 1
  Output 2:              
 2
        


Example Explanation
Explanation 1:
 All X's belong to single shapes
  Explanation 2:              
 Both X's belong to different shapes"""



 from collections import deque
class Solution:
	# @param A : list of strings
	# @return an integer
	@staticmethod
	def removeadj(A, cur, n, m):
        q = deque()
        q.append(cur)
        visited = {cur}
        
        dir_ = {(0,-1),(-1,0),(1,0),(0,1)}
        while q:
            i,j = q.popleft()
            A[i][j] = 'O'
            for l,r in dir_:
                if 0 <= i+l < n and 0<=j+r<m and A[i+l][j+r] == 'X' and (i+l,j+r) not in visited:
                    q.append((i+l, r+j))
                    visited.add((i+l,j+r))
	
	def black(self, A):
        n, m = len(A), len(A[0])
        A = [list(i) for i in A]
        ans = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'X':
                    ans += 1
                    self.removeadj(A, (i,j), n,m)
                    
                    
        return ans
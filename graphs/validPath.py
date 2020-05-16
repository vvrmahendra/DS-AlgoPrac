"""Valid Path
Problem Description
There is a rectangle with left bottom as (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.  Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.   Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.   


Problem Constraints
0 <= x , y, R <= 100 1 <= N <= 1000 Center of each circle would lie within the grid   


Input Format
1st argument given is an Integer x. 2nd argument given is an Integer y. 3rd argument given is an Integer N, number of circles. 4th argument given is an Integer R, radius of each circle. 5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle 6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle   


Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).


Example Input
Input 1:
x = 2
y = 3
N = 1
R = 1
A = [2]
B = [3]
  Input 2:        
 
x = 1
y = 1
N = 1
R = 1
A = [1]
B = [1]
     


Example Output
Output 1:
 NO
  Output 2:        
 NO
     


Example Explanation
Explanation 1:
 There is NO valid path in this case
  Explanation 2:        
 There is NO valid path in this case"""


from collections import deque
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
	@staticmethod
	def possiblePoints(x,y, n, r,E,F):
        def helper(i,j):
            for c in range(n):
                if (E[c]-i)**2+(F[c]-j)**2 <= r**2:
                    return False
                    
            return True
            
        return set([(i,j) for i in range(x+1) for j in range(y+1) if helper(i,j)])
	            
	def solve(self, A, B, C, D, E, F):
        poss = self.possiblePoints(A,B,C,D,E,F)
        if (A,B) not in poss:
            return 'NO'
        q = deque()
        q.append((0,0))
        visited = {(0,0)}
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            i, j = q.popleft()
            if (i,j) == (A,B):
                return 'YES'
                
            for l,r in dir_:
                x,y = l+i, r+j
                if 0<=x<=A and 0 <=y<=B and (x,y) in poss and (x,y) not in visited:
                    q.append((x,y))
                    visited.add((x,y))
                    
        return 'NO'
	    

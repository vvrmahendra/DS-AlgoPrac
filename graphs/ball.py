"""Shortest Distance in a Maze
Problem Description
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls. 1 represents a wall in a matrix and 0 represents an empty location in a wall. There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball. Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.    


Problem Constraints
2 <= N, M <= 100 0 <= A[i] <= 1 0 <= B[i][0], C[i][0] < N 0 <= B[i][1], C[i][1] < M     


Input Format
The first argument given is the integer matrix A. The second argument given is an array of integer B. The third argument if an array of integer C.     


Output Format
Return a single integer, the minimum distance required to reach destination


Example Input
Input 1:
A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
  Input 2:            
A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]
       


Example Output
Output 1:
 1
  Output 2:            
 1
       


Example Explanation
Explanation 1:
 Go directly from start to destination in distance 1.
  Explanation 2:            
 Go directly from start to destination in distance 1."""


from heapq import *
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i, j = B
        n, m = len(A), len(A[0])
        heap = [(0,i,j)]
        heapify(heap)
        dir_ = [(1,0),(0,-1),(-1,0),(0,1)]
        visited = {(i,j)}
        while heap:
            w, i, j = heappop(heap)
            if [i,j] == C:
                return w
                
            for u,l in dir_:
                x, y = i, j
                while 0 <=x < n  and 0<=y < m and A[x][y] != 1:
                    x += u
                    y += l
                    
                x -= u
                y -= l
                if (x,y) not in visited:
                    visited.add((x,y))
                    heappush(heap,(w+abs(x-i)+abs(y-j), x,y))
                
        return -1

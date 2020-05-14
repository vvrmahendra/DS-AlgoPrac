"""Largest Distance between nodes of a Tree
Problem Description
Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree). The nodes will be numbered 0 through N - 1. The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.   


Problem Constraints
2 <= |A| <= 40000


Input Format
First and only argument is vector A


Output Format
Return the length of the longest path


Example Input
Input 1:
 
A = [-1, 0]
  Input 2:        
 
A = [-1, 0, 0]
     


Example Output
Output 1:
 2
  Output 2:        
 3
     


Example Explanation
Explanation 1:
 Path is 0 -> 1.
  Explanation 2:        
 Path is 1 -> 0 -> 2."""

from collections import defaultdict, deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    if len(A) <= 1: return 0
        tree = defaultdict(list)
        for p,c in enumerate(A[1:]):
            tree[p+1].append(c)
            tree[c].append(p+1)
            
        first = 0
        d = 0
        q = deque()
        q.append((0,0))
        visited = set()
        while q:
            cur, dep = q.popleft()
            visited.add(cur)
            if dep > d:
                d = dep
                first = cur
                
            for nei in tree[cur]:
                if nei not in visited:
                    q.append((nei, dep+1))
                    
        
        q.append((first,0))
        visited = set()
        second = first
        d = 0
        while q:
            cur, dep = q.popleft()
            visited.add(cur)
            if dep > d:
                d = dep
                second = cur
                
            for nei in tree[cur]:
                if nei not in visited:
                    q.append((nei, dep+1))
                    
        return d
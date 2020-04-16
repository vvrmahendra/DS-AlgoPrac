"""Range Minimum Query
Problem Description
Given an integer array A of size N. You have to perform two types of query, in each query you are given three integers x,y,z.  
If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive. Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.  


Problem Constraints
1 <= N,M <= 105 1 <= A[i] <= 109 If x = 0, 1<= y <= N and 1 <= z <= 109 If x = 1, 1<= y <= z <= N  


Input Format
First argument is an integer array A of size N. Second argument is a 2-D array B of size M x 3 denoting queries.  


Output Format
Return an integer array denoting the output of each query where value of x is 1.


Example Input
Input 1:
 A = [1, 4, 1]
 B = [ [1, 1, 3],
       [0, 1, 5],
       [1, 1, 2] ]
Input 2:
 A = [5, 4, 5, 7]
 B = [ [1, 2, 4],
       [0, 1, 2],
       [1, 1, 4] ]
 


Example Output
Output 1:
 [1, 4]
Output 2:
 [4, 2]
 


Example Explanation
Explanation 1:
 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.
Explanation 2:
 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.


 """
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def createTree(self, s, e, ind, Tree, A):
        if s == e:
            Tree[ind] = A[s]
            return
        mid = (s+e)//2
        self.createTree(s,mid,2*ind+1, Tree, A)
        self.createTree(mid+1, e, 2*ind+2, Tree, A)
        Tree[ind] = min(Tree[2*ind+1],Tree[2*ind+2])
        return
    
    def getMin(self, qs, qe, s, e, ind, Tree):
        if qs <= s and qe >= e:
            return Tree[ind]
        if qs > e or qe < s:
            return float('inf')
            
        mid = (s+e)//2
            
        left = self.getMin(qs, qe, s, mid, 2*ind+1, Tree)
        right = self.getMin(qs, qe, mid+1, e, 2*ind+2, Tree)
        return min(left, right)
        
    def update(self, ind, value, sind, s, e, Tree):
        from collections import deque
        S = deque()
        S.append(sind)
        while True:
            mid = (s+e)//2
            if ind <= mid:
                e = mid
                sind = 2*sind+1
                S.append(sind)
            elif ind > mid:
                s = mid+1
                sind  = 2*sind+2
                S.append(sind)
            if s == e:
                break
        
        temp = S.pop()
        Tree[temp] = value
        
        while S:
            temp = S.pop()
            Tree[temp] = min(Tree[2*temp+1], Tree[2*temp+2])

        return
    
    def solve(self, A, B):
        n = len(A)
        Tree = [0]*(4*n)
        self.createTree(0, n-1, 0, Tree, A)
        ans = []
        for q in B:
            if q[0] == 0:
                if 1<=q[1]<=n:
                    self.update(q[1]-1, q[2], 0, 0, n-1, Tree)
                    A[q[1]-1] = q[2]
                    # self.createTree(0,n-1,0,Tree,A)
            elif q[0] == 1:
                ans.append(self.getMin(q[1]-1,q[2]-1,0,n-1,0,Tree))
                
        return ans
        
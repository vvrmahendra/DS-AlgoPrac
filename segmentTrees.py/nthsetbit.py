"""Binary updates
Problem Description
Given an integer A denoting the size of the array consisting all ones. You are given Q queries, for each query there are two integer x and y:
If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: Your Solution may run on multiple test cases. NOTE 2: There will atleast 1 query where value of x is 1. 


Problem Constraints
1 <= A, Q <= 106 0 <= x <= 1 1 <= y <= A   


Input Format
First argument is an integer A denoting the size of array. Second argument is a 2-D array B of size Q x 2 where B[i][0] denotes x and B[i][1] denotes y.   


Output Format
Return an integer array denoting the output of each query where x is 1.


Example Input
Input 1:
 A = 4
 B = [ [1, 2],
       [0, 2],
       [1, 4] ]
Input 2:
 A = 5
 B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ] 
  


Example Output
Output 1:
 [2, -1]
Output 2:
 [5, -1]
  


Example Explanation
Explanation 1:
 Initially array = [1, 1, 1, 1]. For first query 2nd one is at index 2.
 After Second query array becomes [1, 0, 1, 1].
 For third query there is no 4th one.
Explanation 2:
 Initially array = [1, 1, 1, 1, 1]. After first query array becomes [1, 1, 0, 1, 1].
 For second query 4th one is at index 5.    
 After third query array remains same [1, 1, 0, 1, 1].
 For fourth query there is no 5th one."""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def __init__(self):
        self.A = None
        self.Tree = None
        self.n = None

    def createTree(self, s, e, sind):
        if s==e:
            self.Tree[sind] = self.A[s]
            return
        mid = (s+e)//2
        self.createTree(s, mid, 2*sind+1)
        self.createTree(mid+1, e, 2*sind+2)
        self.Tree[sind] = self.Tree[2*sind+1]+self.Tree[2*sind+2]
        return
    
    def updateTree(self, ind, val, s, e, sind):
        if s == e == ind:
            self.Tree[sind] = val
            return
        mid = (s+e)//2
        if ind <= mid:
            self.updateTree(ind, val, s, mid, 2*sind+1)
        else:
            self.updateTree(ind, val, mid+1, e, 2*sind+2)
            
        self.Tree[sind] = self.Tree[2*sind+1]+self.Tree[2*sind+2]
        return
    
    def search(self, s, e, ind, sind):
        if s==e:
            return s
        leftOnes = self.Tree[2*sind+1]
        mid = (s+e)//2
        if ind <= leftOnes:
            return self.search(s, mid, ind, 2*sind+1)
            
        else:
            return self.search(mid+1, e, ind-leftOnes, 2*sind+2)
            
        
    def solve(self, A, B):
        self.A = [1]*A
        self.n = A
        self.Tree = [0]*(4*A)
        self.createTree(0, A-1, 0)
        ans = []
        for q in B:
            if q[0] == 0:
                if self.A[q[1]-1] == 1:
                    self.n -= 1
                    self.A[q[1]-1] = 0
                    self.updateTree(q[1]-1, 0, 0, A-1, 0)
                
            if q[0] == 1:
                temp = -2
                if 1<=q[1] <= self.n:
                    temp = self.search(0, A-1, q[1], 0)
                ans.append(temp+1)
                
        return ans
                
                
        
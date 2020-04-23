"""segment tree?
Problem Description
Given an array A of size N and Q queries. Perform following queries:
1 V 0 append V in the back of array.
2 X V set A[X] = V.
3 X 0 delete A[X]. Note: All element at back of X move forward to occupy void.
4 X Y find sum in range [X, Y].
NOTE: For the query of type 4 X Y, output the sum % 109 + 7.    


Problem Constraints
1 <= N,Q <= 100000 1 <= A[i],V <=100000 1 <= X,Y <= N' Where, N' is current size of array.    


Input Format
First argument contains an integer array A. Second argument contains a Q x 3 Matrix B.    


Output Format
Return an integer array containing answer to all query of type 4 X Y in chronological order.


Example Input
 A = [1, 2, 5, 3, 4] 
 B = [ [4, 2, 4], 
       [3, 3, 0],
       [1, 6, 0],
       [4, 3, 5] ]


Example Output
 [10, 13]


Example Explanation
 First Query find sum(A[2],A[3],A[4])
 Second Query make A = [1, 2, 3, 4]
 Third Query make A = [1, 2, 3, 4, 6]
 Fourth Query find sum(A[3],A[4],A[5])
"""
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    # def --init__(self):
    #     self.st = None
    #     self.A = None
    #     self.dele = None
        
    def createTree(self, st, A, s, e, sind):
        if s == e:
            st[sind] = A[s]
            return
        mid = (s+e)//2
        self.createTree(st, A, s, mid, 2*sind+1)
        self.createTree(st, A, mid+1, e, 2*sind+2)
        st[sind] = st[sind*2+1]+st[sind*2+2]
        return
    
    def getRange(self, st,  s, e, qs, qe, sind):
        if qs <= s and qe >= e:
            return st[sind]
        if qe < s or qs > e:
            return 0
            
        mid = (s+e)//2
        left = self.getRange(st, s, mid, qs, qe, 2*sind+1)
        right = self.getRange(st, mid+1, e, qs, qe, 2*sind+2)
        return (left+right)
        
    def update(self, st, s, e, sind, ind, val):
        if s == e:
            st[sind] = val
            return
        mid = (s+e)//2
        if ind <= mid:
            self.update(st, s, mid, 2*sind+1, ind, val)
        else:
            self.update(st,  mid+1, e, 2*sind+2, ind, val)
        st[sind] = st[sind*2+1]+st[sind*2+2]
        
    def getindex(self, st, s, e, sind, i):
        if s == e:
            return s
        leftOnes = st[2*sind+1]
        mid = (s+e)//2
        if i <= leftOnes:
            return self.getindex(st, s, mid, 2*sind+1, i)
        else:
            return self.getindex(st, mid+1, e, 2*sind+2, i-leftOnes)
        
    def solve(self, A, B):
        mod = 10**9+7
        n1 = len(A)
        n = len(A)+len(B)
        A = A+[0]*len(B)
        st = [0]*(4*n)
        de = [1]*n
        dest = [0]*(4*n)
        self.createTree(st, A, 0, n-1, 0)
        self.createTree(dest, de, 0, n-1, 0)
        ans = []
        for q in B:
            if q[0] == 1:
                temp = self.getindex(dest, 0, n-1, 0, n1+1)
                self.update(st,0, n-1, 0, temp, q[1])
                n1 += 1
                A[temp] = q[1]
                
            if q[0] == 2:
                if 1 <= q[1]<=n1:
                    temp = self.getindex(dest, 0, n-1,0, q[1])
                    self.update(st,0, n-1, 0, temp, q[2])
                    A[temp] = q[2]
            
            if q[0] == 3:
                if 1 <= q[1]<=n1:
                    temp = self.getindex(dest, 0, n-1,0, q[1])
                    self.update(st,0, n-1, 0, temp, 0)
                    self.update(dest, 0, n-1, 0, temp, 0)
                    de[temp] = 0
                    n1 -= 1
                    A[temp] = 0
                    
            if q[0] == 4:
                qs = self.getindex(dest, 0, n-1,0, q[1])
                qe = self.getindex(dest, 0, n-1,0, q[2])
                ans.append(self.getRange(st,  0, n-1, qs, qe, 0)%mod)
        # print(A)        
        return ans
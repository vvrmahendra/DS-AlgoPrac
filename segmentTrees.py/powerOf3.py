"""Power of 3
Given a binary string A of size N and an integer matrix B of size Q x 3. Matrix B had Q queries:
For queries of type B[i][0] = 1, flip the value at index B[i][1] in A if and only if the value at that index is 0 and return -1.
For queries of type B[i][0] = 0, Return the value of the binary string from index B[i][1] to B[i][2] modulo 3.
Note: Rows are numbered from top to bottom and columns are numbered from left to right. 
Input Format
The first argument given is the string A.
The second argument given is the integer matrix B.
Output Format
Return an array of size Q where ith value is answer to ith query.
Constraints
1 <= N <= 100000
1 <= Q <= 200000
1 <= B[i][1], B[i][2] <= N
B[i][1] <= B[i][2]
For Example
Input 1:
    A = 10010
    B = [ [0, 3, 5]
          [0, 3, 4]
          [1, 2, -1]
          [0, 1, 5]
          [1, 2, -1]
          [0, 1, 4] ]
Output 1:
    [2, 1, -1, 2, -1, 1]"""



class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def __init__(self):
        self.A = None
        self.Tree = None
    def createTree(self, s, e, sind):
        if s == e :
            self.Tree[sind] = int(self.A[s])
            return
        mid = (s+e)//2
        self.createTree(s,mid,2*sind+1)
        self.createTree(mid+1,e,2*sind+2)
        if (e-mid)%2 == 1:
            self.Tree[sind] = (2*self.Tree[2*sind+1]+self.Tree[2*sind+2])%3
        else:
            self.Tree[sind] = (self.Tree[2*sind+1]+self.Tree[2*sind+2])%3
        return
    
    def getRange(self, s, e, qs, qe, sind):
        if qs <= s and qe >= e:
            return self.Tree[sind]
        if qs > e or qe < s:
            return 0
            
        mid = (s+e)//2
        if qe <= mid:
            return self.getRange(s,mid, qs, qe,2*sind+1)
        elif qs > mid:
            return self.getRange(mid+1, e, qs, qe, 2*sind+2)
        
        left = self.getRange(s,mid, qs,mid,2*sind+1)
        right = self.getRange(mid+1, e, mid+1, qe, 2*sind+2)
        if (qe-mid)%2 == 1:
            return (2*left+right)%3 
        else:
            return (left+right)%3
            
    def updateBit(self, ind, val, s, e, sind):
        if s == e == ind:
            self.Tree[sind] = val
            return
        mid = (s+e)//2
        if ind <= mid:
            self.updateBit(ind, val, s, mid, 2*sind+1)
        else:
            self.updateBit(ind, val, mid+1, e, 2*sind+2)
            
        if (e-mid)%2 == 1:
            self.Tree[sind] = (2*self.Tree[2*sind+1]+self.Tree[2*sind+2])%3
        else:
            self.Tree[sind] = (self.Tree[2*sind+1]+self.Tree[2*sind+2])%3
        return
            
    def solve(self, A, B):
        self.A = list(A)
        self.Tree = [0]*4*len(A)
        self.createTree(0,len(A)-1, 0)
        ans = []
        for q in B:
            if q[0] == 0:
                temp = self.getRange(0, len(A)-1, q[1]-1, q[2]-1,0)
                ans.append(temp)
            if q[0] == 1:
                if 1<=q[1]<=len(A) and self.A[q[1]-1] == '0':
                    self.updateBit(q[1]-1, 1, 0, len(A)-1, 0)
                    self.A[q[1]-1] == '1'
                ans.append(-1)
                
        return ans
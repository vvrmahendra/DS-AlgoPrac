"""Connect ropes with minimum length
Given an array of integers A representing the length of ropes. You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths. You need to connect the ropes with minimum cost. Find and return the minimum cost to connect these ropes into one rope. 
Input Format
The only argument given is the integer array A.
Output Format
Return the minimum cost to connect these ropes into one rope.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^3
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    33
Explanation 1:
    1 + 2 = 3
    3 + 3 = 6
    4 + 5 = 9
    6 + 9 = 15

    3 + 6 + 9 + 15 = 33

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    182
Explanation 2:
    5 + 11 = 16
    16 + 17 = 33
    33 + 100 = 133

    16 + 33 + 133 = 182
"""



class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.A = None
        
    def heapify(self, i):
        n = len(self.A)
        while True:
            small = i
            l = 2*i+1
            r = 2*i+2
            if l < n and self.A[l] < self.A[small]:
                small = l
            if r < n and self.A[r] < self.A[small]:
                small = r
                
            if small == i:
                break
            else:
                self.A[i], self.A[small] = self.A[small], self.A[i]
                i = small
                
    def buildHeap(self):
        n = len(self.A)
        leaf = (n+1)//2
        p = n-leaf-1
        for i in range(p, -1, -1):
            self.heapify(i)
        
    def insert(self, val):
        self.A.append(val)
        ch = len(self.A)-1
        while True:
            pa = (ch-1)//2
            if self.A[pa] > self.A[ch] and pa >= 0:
                self.A[pa], self.A[ch] = self.A[ch], self.A[pa]
                ch = pa
            else:
                break
            
    def delete(self):
        ans = self.A[0]
        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify(0)
        return ans
        
    def solve(self, A):
        if len(A) <= 2: return sum(A)
        self.A = A
        self.buildHeap()
        ans = 0
        while len(self.A) >=2:
            first = self.delete()
            second = self.delete()
            ans += (first+second)
            self.insert(first+second)
            
        return ans





#Using HeapQ library
class Solution2:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) <= 2: return sum(A)
        import heapq as hq
        hq.heapify(A)
        ans = 0
        while len(A) >= 2:
            first = hq.heappop(A)
            second = hq.heappop(A)
            ans += first+second
            hq.heappush(A, first+second)
        return ans
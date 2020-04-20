"""Ways to form Max Heap 2
Max heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes. If you want to know more about Heaps, please visit this link. So now the problem statement for the question is: Given an array of size n consisting of n-1 distinct elements.In other words there is exactly one element that is repeated.It is given that the element that would repeat would be either the maximum element or the minimum element. Find the number of structurally different max heaps possible using all the n elements of the array that is max heap of size n. Let us take an example with array array elements as
1 5 5
The possible max heaps using the given elements are:- First: 5 on the root. 1 as the left child of root and 5 as the right child of the root
    5
  /   \
1       5
Second: 5 on the root. 5 as the left child of root and 1 as the right child of the root.
    5
  /   \
5       1
There are only two structurally different max heaps using the given array elements. Implement the below function to return the number of distinct max heaps of size n. As final answer can be very large output your answer modulo 1000000007. Input constraints: n<=1000."""


from math import log2
class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.dp = {}
        self.dp2 = {}

    @staticmethod
    def nCl(n,l):
        if n-l < l:
            l = n-l
            
        num = 1
        den = 1
        for i in range(l):
            num = num*(n-i)
            den = den*(i+1)
            
        return num//den
        
    def helper1(self, A):
        mod = 10**9+7
        if A in self.dp:
            return(self.dp[A])
        if A == 1:
            return 1
        if A == 0:
            return 1
        h = int(log2(A))+1
        lI = 2**(h-2)-1
        lO = min(2**(h-2), A-(2**(h-1)-1))
        l = lI+lO
        r = A-l-1
        # print(l,r)
        res =  self.nCl(A-1,l)*self.helper1(l)*self.helper1(r)
        self.dp[A] = res
        # print(self.dp)
        return res
        
    def helper2(self, A):
        mod = 10**9+7
        if A in self.dp2:
            return self.dp2[A]
        
        if A <= 3:
            return 1
        if A == 4:
            return 2
        
        h = int(log2(A))+1
        lI = 2**(h-2)-1
        lO = min(2**(h-2), A-(2**(h-1)-1))
        l = lI+lO
        r = A-l-1
        res1 = self.nCl(A-3, l-2)*self.helper2(l)*self.helper1(r)
        res2 = self.nCl(A-3, l)*self.helper1(l)*self.helper2(r) if A-3 >= l else 0
        res3 = self.nCl(A-3, l-1)*self.helper1(l)*self.helper1(r)
        res = (res1+res2+res3)
	    self.dp2[A] = res
	    return res
	    
    def solve(self, A):
        mod = 10**9+7
        import heapq as hq
        hq.heapify(A)
        n = len(A)
        first = hq.heappop(A)
        second = hq.heappop(A)
        if first == second:
            return self.helper2(n)%mod
        else:
            return self.helper1(n)%mod

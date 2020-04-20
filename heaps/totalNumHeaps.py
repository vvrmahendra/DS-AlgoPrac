"""Ways to form Max Heap
Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes. If you want to know more about Heaps, please visit this link So now the problem statement for this question is: How many distinct Max Heap can be made from n distinct integers In short, you have to ensure the following properties for the max heap :
Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. )
Every node is greater than all its children
Let us take an example of 4 distinct integers. Without loss of generality let us take 1 2 3 4 as our 4 distinct integers Following are the possible max heaps from these 4 numbers :
         4 
       /  \ 
      3   2 
     / 
    1
         4 
       /  \ 
      2   3 
     / 
    1
        4 
       /  \ 
      3   1 
     / 
    2
These are the only possible 3 distinct max heaps possible for 4 distinct elements. Implement the below function to return the number of distinct Max Heaps that is possible from n distinct elements. As the final answer can be very large output your answer modulo 1000000007 Input Constraints : n <= 100"""


from math import log2
class Solution:
	# @param A : integer
	# @return an integer
	def __init__(self):
	    self.dp = {}
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
        
        
	def solve(self, A):
        	    
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
        res =  self.nCl(A-1,l)*self.solve(l)*self.solve(r)
        self.dp[A] = res
        # print(self.dp)
        mod = 10**9+7
        return res%mod
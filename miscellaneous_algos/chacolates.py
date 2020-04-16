"""Magician and Chocolates
Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates. Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time. For example,
K = 3
N = 2
A = 6 5

Return: 14
At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate so, total number of chocolates eaten: 6 + 5 + 3 = 14 Note: Return your answer modulo 10^9+7"""
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
	    A, B = B, A
	    if not A: return 0
        import heapq as hq
        A = [-1*i for i in A]
        hq.heapify(A)
        ans = 0
        mod = 10**9+7
        for i in range(B):
            temp = hq.heappop(A)
            if temp == 0:
                return ans
            # print(temp)    
            ans = (ans-temp)%mod
            hq.heappush(A, -1*((-1*temp)//2))
            
        
        return ans%mod
"""given an integer A, find the Ath smallest number which has exactly 8 set bits
example:- 1 -> 255
example:- 3 -> 447"""


from functools import lru_cache
from fractions import Fraction
class Solution:
    # @param A : integer
    # @return a strings
    @lru_cache(maxsize = None)
    def ncr(self,n,r):
        ans = Fraction(1,1)
        if n-r < r:
            r = n-r
            
        for i in range(r):
            ans = ans * (n-i)/(i+1)
            
        return int(ans)
        
            
    def solve(self, A):
        n = 8
        while self.ncr(n,8) < A:
            n += 1
        n += 1    
        arr = ['0']*n
        ones = 0
        zeros = 0
        # print(n)
        for i in range(n):
            sig = n-i
            temp = self.ncr(sig-1, 8-ones)
            
            if temp == A:
                # print('one',i,temp)
                arr[i] = '0'
                for i in range(i+1, i+1+8-ones):
                    arr[i] = '1'
                    
                break
            
            if temp < A:
                # print('two',i,temp)
                arr[i] = '1'
                ones += 1
                A = A-temp
                
            else:
                # print('three',i,temp)
                arr[i] = '0'
                zeros += 1
                
            
                
        # print(arr)       
        return int("".join(arr),2)
            
        
        
"""Open minimum shops
Problem Description
There are A shops numbered 1 to A and B items numbered 1 to B. Shop contains different items denoted by 2-D array C of size N x 2 where C[i][0] denotes shop number and C[i][1] denotes item number. There are D people number 1 to D which wants to buy item.
Need of the people is denoted by a 2-D array E of size M x 2 where E[i][0] denotes person number and E[i][1] denotes item number. Find the minimum number of shops that needs to be opened such that demand of each and every person is fulfilled. Return -1 if not possible. NOTE: The shopkeeper has an infinte number of supplies for the item number he contains.      


Problem Constraints
1 <= A, B, D <= 20
1 <= N, M <= 400


Input Format
First argument is an integer A denoting number of shops.
Second argument is an integer B denoting number of items.
Third argument is a 2-D array C of size N x 2 denoting the items shop contains.
Fourth argument is an integer D denoting the number of people.
Fifth argument is a 2-D array E of size M x 2 denoting the items people need.


Output Format
Return an integer denoting the minimum number of shops needs to be opened such that demand of each and every person is fulfilled. Return -1 if not possible.


Example Input
Input 1:
 A = 4
 B = 5
 C = [ [1, 2],
       [1, 3],
       [2, 1],
       [2, 2],
       [3, 4] ]
 D = 4
 E = [ [1, 3],
       [1, 2],
       [2, 3],
       [2, 1],
       [4, 1] ]
Input 2:
 A = 2
 B = 3
 C = [ [1, 2], 
       [2, 1] ]
 D = 2
 E = [ [1, 2],
       [2, 3],
       [2, 1] ]


Example Output
Output 1:
 2
Output 2:
 -1
     


Example Explanation
Explanation 1:
 Each shopkeeper has the following items: 
 Shop 1 : [2, 3]
 Shop 2 : [1, 2]
 Shop 3 : [4]
 Shop 4 : [] (has nothing)
 Items we need = [1, 2, 3]
 We need 2 shops i.e Shop 1 and 2, to be kept open so that demands of all people is satisfied.
Explanation 2:
 Items we need = [1, 2, 3]. 
 No shop has item 3. So will return -1."""


import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @param D : integer
    # @param E : list of list of integers
    # @return an integer
    def countSetBits(self, ele):
        n = int(math.log2(ele))+1
        ans = 0
        for i in range(n):
            if (1<<i) & ele:
                ans += 1
        return ans
    def solve(self, A, B, C, D, E):
        from collections import defaultdict
        merchant = defaultdict(int)
        for m, it in C:
            merchant[1 << (m-1)] += (1<<(it-1))
        
        req = 0
        for p, it in E:
            if (1<<(it-1) & req) == 0:
                req += (1 << (it-1))
            
        ans = []
        for mer in range(2**A-1):
            till = 0
            for bit in range(A):
                till = till | merchant[(1<<bit)&(mer)]
            
            if till & req == req:
                ans.append(mer)
                
        if not ans:
            return -1
            
        return min([self.countSetBits(i) for i in ans])
            
        
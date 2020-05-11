"""1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

113

10

Add to List

Share
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        pre = [0]*(n+1)
        pre[0] = arr[0]
        for i in range(1,n):
            pre[i] = pre[i-1]^arr[i]
            
        ans = 0
        # for j in range(1,n):
        for i in range(n-1):
            for k in range(i+1,n):
                if pre[i-1] == pre[k]: ans += (k-i)
                        
        return ans
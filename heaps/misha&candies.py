"""Misha and Candies
Misha loves eating candies. She has given N boxes of Candies. She decides, every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies. Misha does not like a box if it has the number of candies greater than K so she won't eat from that box. Can you find how many candies she will eat? Note: If a box has an odd number of candies then Misha will eat floor(odd/2)
 Input Format
The first argument is A an Array of Integers, where A[i] is the number of candies in the ith box.
The second argument is K, the maximum number of candies Misha like in a box.
Output Format
Return an Integer X i.e number of candies Misha will eat.
Constraints
1 <= N <= 1e5
1 <= A[i] <= 1e5
1 <= K <= 1e6
For Example
Example Input:
    A = [3, 2, 3]
    k = 4
Example Output:
    2

Explanation:
    1st time Misha will eat from 2nd box, i.e 1 candy she'll eat and will put the remaining 1 candy in the 1st box.
    2nd time she will eat from the 3rd box, i.e 1 candy she'll eat and will put the remaining 2 candies in the 1st box.
    She will not eat from the 3rd box as now it has candies greater than K.
    So the number of candies Misha eat is 2."""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if not A: return 0
        import heapq as hq
        hq.heapify(A)
        ans = 0
        while True:
            # print(A)
            temp = hq.heappop(A)
            if temp > B:
                return ans
            
            eat = temp//2
            ans += eat
            if A:
                next = hq.heappop(A)
                hq.heappush(A, next+temp-eat)
            else:
                return ans
                
        return ans
"""The ship company
Problem Description
The local ship renting service has a special rate plan:
It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
 The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up to A-th person. You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.    


Problem Constraints
1 ≤ A ≤ 3000
1 ≤ B ≤ 1000
1 ≤ C[i] ≤ 1000
It is guaranteed that there are at least A empty seats in total.


Input Format
First argument is a integer A denoting the number of passengers in the queue.
Second arugument is a integer B deonting the number of ships.
Third argument is an integer array C of size B where C[i] denotes the number of empty seats in the i-th ship before the ticket office starts selling tickets.


Output Format
Return an array of size 2 denoting the maximum and minimum money that the ship company can earn.


Example Input
Input 1:
 A = 4
 B = 3
 C = [2, 1, 1]
Input 2:
 A = 4
 B = 3
 C = [2, 2, 2]
  


Example Output
Output 1:
 [5, 5]
Output 2:
[7, 6]
  


Example Explanation
Explantion 1:
 Maximum money can be earned if the passenger choose : 2(first ship) + 1(first ship) + 1(second ship) + 1(third ship).
 So, the cost will be 5.
 Minimum money can be earned if the passenger choose : 1(senocd ship) + 2(first ship) + 1(first ship) + 1(third ship).
 So, the cost will be 5.
Explanation 2:
 Maximum money can be earned if the passenger choose : 2(first ship) + 2(second ship) + 2(third ship) + 1(first ship).
 So, the cost will be 7.
 Minimum money can be earned if the passenger choose : 2(senocd ship) + 2(first ship) + 1(first ship) + 1(second ship).
 So, the cost will be 6."""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        heap1 = [i for i in C]
        heap2 = [-1*i for i in C]
        import heapq as hq
        hq.heapify(heap1)
        hq.heapify(heap2)
        max_ = 0
        min_ = 0
        for i in range(A):
            temp = hq.heappop(heap1)
            min_ += temp
            if temp > 1:
                hq.heappush(heap1, temp-1)
            temp = hq.heappop(heap2)
            max_ -= temp
            if temp < -1:
                hq.heappush(heap2, temp+1)
            
        return [max_, min_]
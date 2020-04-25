"""Let's Party
In Danceland, one person can party either alone or can pair up with another person. Can you find in how many ways they can party if there are N people in Danceland? Input Format
Given only argument A of type Integer, number of people in Danceland.
Output Format
Return a single integer N mod 10003, i.e number of ways people of Danceland can party.
Constraints
1 <= N <= 1e5 
Example Input 1: N = 3 Example Output 1: 4 Explanation 1: Let suppose three people are A, B, and C. There are only 4 ways to party as, (A, B, C) All party alone (AB, C) A and B party together and C party alone (AC, B) A and C party together and B party alone (BC, A) B and C party together and A party alone here 4 % 10003 = 4, so answer is 4."""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 2: return A
        first = 1
        second = 2
        for i in range(A-2):
            temp = (second+(i+2)*first)%10003
            first = second
            second = temp
            
        return second%10003
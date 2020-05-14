"""253. Meeting Rooms II
Medium

2394

41

Add to List

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        a = []
        for s,e in intervals:
            a.append((s,1))
            a.append((e,0))
        a.sort()
        ans = 0
        ite = 0
        for t,f in a:
            if f == 1:
                ite += 1
                ans = max(ans,ite)
            else:
                ite -= 1
                
        return ans
            
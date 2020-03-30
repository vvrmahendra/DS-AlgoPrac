"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def __init__(self):
        self.ans = None
        self.track = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(A,l, dict_):
            global ans
            
            if self.ans:
                return
            if l == len(A):
                self.ans = True
                return
            for ele in dict_:
                if ele == A[l:l+len(ele)]:
                    # if l+len(ele) in self.track:
                    #     return
                    # else:
                    #     self.track[l+len(ele)] = True
                    helper(A,l+len(ele), dict_)
                    
        helper(s,0, wordDict)
        return self.ans
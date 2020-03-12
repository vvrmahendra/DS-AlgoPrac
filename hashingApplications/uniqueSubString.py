"""Longest Substring Without Repeat
Given a string, find the length of the longest substring without repeating characters. 
Example: The longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1."""



def lengthOfLongestSubstring(self, A):
    n = len(A)
    dict_ = {}
    ans = 0
    index_ = 0

    j = 0
    while j < n:
        if A[j] not in dict_:
            dict_[A[j]] = j
            j += 1
        elif dict_[A[j]] < index_:
            dict_[A[j]] = j
            j += 1
            
        else:
            ans = max(ans, j-index_)
            index_ = dict_[A[j]]+1
            dict_[A[j]] = j
            j +=1
            
    ans = max(ans, j-index_)
    return ans
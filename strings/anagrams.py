"""Anagrams
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.
 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' Note: All inputs will be in lower-case. 
Example :
Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4. dog and god are another set of anagrams which correspond to index 2 and 3. The indices are 1 based ( the first element has index 1 instead of index 0).
"""



def anagrams(A):
    def helper(A):
        dict_ = {}
        for i in A:
            if i in dict_:
                dict_[i] += 2
            else:
                dict_[i] = 1
        hashable = frozenset(dict_.items())        
        return hashable
        
    dict_ = {}
    n = len(A)
    ans = []
    index_ = 0
    for i in range(n):
        temp_dict = helper(A[i])
        if temp_dict in dict_:
            ans[dict_[temp_dict]].append(i+1)
        else:
            dict_[temp_dict] = index_
            ans.append([i+1])
            index_ += 1
            
    return ans


def anagramsV2(A):
    from collections import defaultdict
    n = len(A)
    dict_ = defaultdict(int)
    ans = []
    for i in range(n):
        hash_ = 0
        for char_ in A[i]:
            hash_ += ord(char_)**2
            
        if hash_ in dict_:    
            ans[dict_[hash_]].append(i+1)
        else:
            ans.append([i+1])
            dict_[hash_] = len(ans)-1
            
    return ans
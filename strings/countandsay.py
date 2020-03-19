"""The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11. 
11 is read off as two 1s or 21. 
21 is read off as one 2, then one 1 or 1211. 
Given an integer n, generate the nth sequence. 
Note: The sequence of integers will be represented as a string. Example: if n = 2, the sequence is 11."""


def countAndSay(A):
    def helper(str_):
        n = len(str_)
        i = 0
        ans = ""
        while i < n:
            temp = 1
            temp_alpha = str_[i]
            while i < n-1 and str_[i] == str_[i+1]:
                temp = temp+1
                i = i+1
            i = i+1    
            ans = ans+str(temp)+temp_alpha
            
        return ans
    seq = '1'
    n = 1
    while n < A:
        seq = helper(seq)
        n += 1
        
    return seq
                
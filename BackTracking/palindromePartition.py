"""Given a string s, partition s such that every string of the partition is a palindrome.
 Return all possible palindrome partitioning of s. Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))

Example Input
Input 1:
s = "aab"
  


Example Output
Output 1:
 [
    ["a","a","b"]
    ["aa","b"],
  ]"""


ans = []
def isPalindrome(str_):
    n = len(str_)
    i = 0
    j = n-1
    while i <= j:
        if str_[i] != str_[j]:
            return False
        
        i += 1
        j -= 1
    
    return True


def generation(A,values):
    if len(A) == 0:
        for ele in values:
            check = isPalindrome(ele)
            if not check:
                return
            
        global ans
        temp = []
        for ele in values:
            temp.append(ele)
        ans.append(temp)
        
        return
    
    last_value = values[-1]
    values[-1] = last_value+A[0]
    generation(A[1:],values)
    values[-1] = last_value
        
    values.append(A[0])
    generation(A[1:],values)
    values.pop()
    return

if __name__ == "__main__":
    A = "efe"
    generation(A[1:],[A[0]])
    ans.sort()
    print(ans)
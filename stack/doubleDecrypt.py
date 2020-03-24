"""kth character in double decrypted string
Given a String A and an integer B. String A is encoded consisting of lowercase English letters and numbers.
A is encoded in a way where repetitions of substrings are represented as substring followed by the count of substrings. 
For example: if the encrypted string is “ab2cd2” and B=6, so the output will be ‘d’ because the decrypted string is “ababcdababcd” and 4th character is ‘b’. 
You have to find and return the Bth character in the decrypted string. 
Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times. No leading 0 is present in the frequency of substring. 
Input Format
The arguments given are string A and integer B.
Output Format
Return the Bth character in the decrypted string.
Constraints
1 <= length of the array <= 10^5
1 < = K < = 10^9
For Example
Input 1:
    A = "ab2c3"
    B = 8
Output 1:
    a
    Decrypted string will be "ababcababcababc" and 'a' is the 8th character.

Input 2:
    A = "x2y3"
    B = 3
Output 2:
    y
    Decrypted string will be 'xxyxxyxxy' """


def solve(A, B):
    s = []
    len_ = 0
    n = len(A)
    i = 0
    while i < n and len_<=B:
        chunk = 0
        # print(A[i])
        while i < n and A[i].isdigit():
            chunk = chunk * 10 + int(A[i])
            i += 1
        if chunk:
            len_ = len_*chunk
            chunk = 0
        else:
            len_ = len_+1
            s.append([i, len_])
            i += 1
            
    # print(s)
    while s:
        temp = s.pop()
        if not B%temp[1]:
            return A[temp[0]]
        else:
            B = B%temp[1]
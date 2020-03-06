"""Gray Code
Problem Description
The gray code is a binary numeral system where two successive values differ in only one bit.
 Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0. 


Problem Constraints
1 <= n <= 16


Input Format
First argument is an integer n.


Output Format
Return an array of integers representing the gray code sequence.


Example Input
Input 1:
2
 


Example Output
output 1:
[0,1,3,2]
"""




def graycode(n):
    ans = [0,1]
    for i in range(1,n):
        temp = []
        for j in ans:
            temp.append(j)
        for j in ans[::-1]:
            temp.append(2**i+j)
        ans = temp
        
    return ans

if __name__ == "__main__":
    ans = graycode(3)
    print(ans)
Alternate positive and negative elements
Problem Description
"""Given an array of integers A, arrange them in an alternate fashion such that every non-negative number is followed by negative and vice-versa, starting from a negative number, maintaining the order of appearance. The number of non-negative and negative numbers need not be equal. If there are more non-negative numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array. Note: Try solving with O(1) extra space. 


Problem Constraints
1 <= length of the array <= 7000
-10^9 <= A[i] <= 10^9


Input Format
The first argument given is the integer array A.


Output Format
Return the modified array.


Example Input
Input 1:
A = [-1, -2, -3, 4, 5]
Input 2:
A = [5, -17, -100, -11]


Example Output
Output 1:
[-1, 4, -2, 5, -3]
Output 2:
[-17, 5, -100, -11]


Example Explanation
Explanation 1:
A = [-1, -2, -3, 4, 5]
Move 4 in between -1 and -2, A => [-1, 4, -2, -3, 5]
Move 5 in between -2 and -3, A => [-1, 4, -2, 5, -3]
"""




def roundArray(A,i,j):
    temp = A[j]
    for index_ in range(j,i,-1):
        A[index_] = A[index_-1]
    A[i] = temp

def negPos(A):
    n = len(A)
    i = 0
    j = 0
    while j < n:
        print(j)
        if j%2 == 0 and A[j] < 0:
            print("first")
            j += 1
            i += 1
        elif j%2 == 1 and A[j] >= 0:
            print(j,"second")
            j += 1
            i += 1
            
        elif j%2 == 1 and A[j] < 0:
            print("third")
            while j < n and A[j] < 0:
                j +=1
            if j == n:
                return
            roundArray(A,i,j)
            i += 1
            j = i
            
        elif j%2 == 0 and A[j] >= 0:
            print("fourth")
            while j < n and A[j] >= 0:
                j += 1
            if j == n:
                return
            roundArray(A,i,j)
            i += 1
            j = i
            
    return
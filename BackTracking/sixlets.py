"""Problem Description
Given a array of integers A of size N and an integer B. Return number of non-empty subsequences of A of size B having sum <= 1000. 


Problem Constraints
1 <= N <= 20 1 <= A[i] <= 1000 1 <= B <= N 


Input Format
The first argument given is the integer array A. The second argument given is the integer B. 


Output Format
Return number of subsequences of A of size B having sum <= 1000.


Example Input
Input 1:
    A = [1, 2, 8]
    B = 2
Input 2:
    A = [5, 17, 1000, 11]
    B = 4


Example Output
Output 1:
3
Output 2:
0


Example Explanation
Explanation 1:
 {1, 2}, {1, 8}, {2, 8}
"""










ans = 0
def comb(A,B,sum_,number):
    if number == B:
        if sum_ <= 1000:
            global ans
            ans += 1
        return
    if sum_ > 1000:
        return
    if number > B:
        return
    if len(A) == 0:
        return
    
    sum_ += A[0]
    number = number+1
    comb(A[1:],B,sum_,number)
    number = number-1
    sum_ -= A[0]
    comb(A[1:],B,sum_,number)
    return

if __name__ == "__main__":
    A = [5, 17, 1000, 11]
    B = 4
    comb(A,B,0,0)
    print(ans)
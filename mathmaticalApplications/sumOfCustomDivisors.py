"""Number of divisors
Max. Marks: 100
You are given two numbers n and k. For each number in the interval [1, n], your task is to calculate its largest divisor that is not divisible by k. Print the sum of these divisors.

Note: k is a prime number.

Input format

The first line contains an integer T representing the number of test cases that will follow.
Each test case consists of one line containing two integers n and k.
Output format

The output must contain the answer for each test case on a different line.

Each answer consists of a single integer.

Constraints


 

SAMPLE INPUT 
4
10 3
10 2
10 5
1000000000 97
SAMPLE OUTPUT 
41
36
43
494897959532893312
Explanation
In the first test case, f (x) from 1 to 10 is [1, 2, 1, 4, 5, 2, 7, 8, 1, 10], sum of which is 41.

In the second test case, f (x) from 1 to 10 is [1, 1, 3, 1, 5, 3, 7, 1, 9, 5].

In the third test case, f (x) from 1 to 10 is [1, 2, 3, 4, 1, 6, 7, 8, 9, 2]."""


# https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/k-excess-1-be669e5a/
# Write your code here
def apSum(a, N, common):
    n = N//a
    return common*(n)*(n+1)//2

def answer(N,k):
    ans = N*(N+1)//2
    a = k
    while True:
        
        temp = apSum(a,N, k-1)
        if temp == 0:
            return ans
        ans = ans-temp
        a = a*k

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,k = input().split()
        n,k = int(n),int(k)
        print(answer(n,k))
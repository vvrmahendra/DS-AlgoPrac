def helper(n, dp):
    if dp[n] or n <= 0:
        return
    helper(n-1, dp)
    helper(n-2, dp)
    dp[n] = dp[n-1]+dp[n-2]

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    dp = [0]*(n+1)
    dp[1] = 1
    helper(n, dp)
    print(dp[n])
    return 0

if __name__ == '__main__':
    main()
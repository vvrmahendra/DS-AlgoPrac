"""Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


def findNthDigit(n):
    power = 1
    limit = 9
    values = 9
    while n > limit:
        power = power+1
        values = (10**(power)-10**(power-1))*power
        print(values)
        limit += values
    
    limit = limit-values
    target = n-limit
    quo = target//power
    rem = target%power
    # print(limit, target,power, quo, rem)
    if not rem:
        val = 10**(power-1)-1+quo
        return int(str(val)[-1])
    
    val = 10**(power-1)-1+quo+1
    return int(str(val)[rem-1])
    
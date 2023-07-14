#!/usr/bin/python3

def minOperations(n):
    if n < 2:
        return 0
    res = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            res += i
    if n > 1:
        res += n
    return res


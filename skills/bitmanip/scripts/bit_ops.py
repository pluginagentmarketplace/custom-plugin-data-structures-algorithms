#!/usr/bin/env python3
def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result

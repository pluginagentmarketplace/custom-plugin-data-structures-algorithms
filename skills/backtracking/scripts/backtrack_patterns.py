#!/usr/bin/env python3
def permutations(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i, n in enumerate(remaining):
            backtrack(path + [n], remaining[:i] + remaining[i+1:])
    backtrack([], nums)
    return result

def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result

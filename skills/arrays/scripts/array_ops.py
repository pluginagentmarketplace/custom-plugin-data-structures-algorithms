#!/usr/bin/env python3
import json
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen: return [seen[target-n], i]
        seen[n] = i
    return []
if __name__ == "__main__":
    print(json.dumps({"two_sum_example": two_sum([2,7,11,15], 9)}, indent=2))

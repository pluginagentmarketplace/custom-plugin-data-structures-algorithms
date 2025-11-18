---
name: sliding-window-pattern
description: Master sliding window technique for solving subarray and substring problems efficiently with O(n) time complexity.
---

# Sliding Window Pattern

## Core Concept
Maintain a window of elements and slide it across the data structure.

### Fixed Window Size
```python
def maxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_avg = max(max_avg, window_sum / k)

    return max_avg
```

### Variable Window Size
```python
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

## Common Problems
- Longest Substring Without Repeating Characters: O(n)
- Minimum Window Substring: O(n)
- Longest Substring with K Distinct: O(n)
- Max Consecutive Ones III: O(n)

## Time Complexity
- Fixed: O(n)
- Variable: O(n)
- Space: O(1) or O(k) for hash map
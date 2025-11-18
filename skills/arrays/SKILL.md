---
name: array-techniques
description: Master essential array techniques including two pointers, sliding window, and prefix sums for efficient problem solving.
---

# Array Techniques Skill

## Two Pointers Pattern

### Same Direction (Fast/Slow)
```python
def removeElement(nums, val):
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left
```

### Opposite Direction (Converging)
```python
def twoSum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
```

## Sliding Window

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

## Prefix Sum

```python
def sumRange(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    def rangeSum(left, right):
        return prefix[right + 1] - prefix[left]

    return rangeSum
```
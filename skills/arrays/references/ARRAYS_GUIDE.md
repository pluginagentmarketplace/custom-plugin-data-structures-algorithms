# Arrays Guide

## Two Pointers
```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l, r = l + 1, r - 1
    return True
```

## Sliding Window
```python
def max_sum_subarray(arr, k):
    window = sum(arr[:k])
    max_sum = window
    for i in range(k, len(arr)):
        window = window + arr[i] - arr[i-k]
        max_sum = max(max_sum, window)
    return max_sum
```

# Hashing Guide

## Common Patterns
- **Two Sum**: Use map to store complement
- **Group Anagrams**: Sorted string as key
- **Frequency Count**: Counter/defaultdict

```python
# Two Sum O(n)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
        seen[n] = i
```

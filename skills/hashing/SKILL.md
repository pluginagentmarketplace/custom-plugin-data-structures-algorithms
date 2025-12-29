---
name: hashing-techniques
description: Hash-based data structures and techniques including frequency counting, duplicate detection, and LRU cache implementation.
sasmp_version: "1.3.0"
bonded_agent: 01-arrays-lists
bond_type: PRIMARY_BOND
---

# Hashing Techniques Skill

## Frequency Counting Pattern
```python
def topKFrequent(nums, k):
    from collections import Counter
    import heapq

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Alternative: Bucket sort approach
def topKFrequentBucket(nums, k):
    from collections import Counter

    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if len(result) == k:
            break
        result.extend(buckets[i])

    return result[:k]
```

## Duplicate Detection
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

def findDuplicates(nums):
    duplicates = set()
    seen = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# In-place with negative marking
def findDuplicatesInPlace(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(index + 1)
        else:
            nums[index] = -nums[index]
    return duplicates
```

## LRU Cache Implementation
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

## Group Anagrams
```python
def groupAnagrams(strs):
    from collections import defaultdict

    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())
```
---
name: 06-hash-tables
description: Master hash tables, sets, and hash-based data structures for O(1) operations. Covers collision handling, frequency counting, LRU cache, and 35+ problems.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
skills: []
triggers:
  - "dsa hash"
  - "dsa"
  - "leetcode"
capabilities:
  - Hash Maps
  - Hash Sets
  - Collision Handling
  - Frequency Counting
  - Duplicate Detection
  - Group Anagrams
  - LRU Cache
  - Two-Pass Solutions

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [lookup, frequency, duplicate, grouping, cache, pattern]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    data_type:
      type: string
      enum: [integer, string, tuple, custom]
    constraints:
      type: object
      properties:
        max_n: { type: integer, default: 100000 }
        key_space: { type: string, enum: [small, medium, large] }
        order_matters: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        data_structure: { type: string }
        hash_function: { type: string }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    tradeoffs:
      type: string
    edge_cases:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - hash_collision
    - memory_exceeded
    - key_not_hashable

fallback_strategy:
  primary: alternative_hash_function
  secondary: sorted_array_approach
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "HSH"

prerequisites:
  required:
    - array-techniques
  recommended:
    - string-basics

bonded_skills:
  primary: hashing-techniques
  secondary: []
---

# 🗃️ Hash Tables & Sets Master Agent

**O(1) Lookup Mastery** — Production-Grade v2.0

Hash tables provide constant-time operations for lookup, insertion, and deletion. Master them to transform O(n) problems into O(1).

## 🎯 Core Competencies

### Hash Table Fundamentals
```
Hash Function: key → index (bucket)
Collision Handling:
  1. Chaining: Linked list at each bucket
  2. Open Addressing: Linear/quadratic probing

Complexity (Average):
  - Insert: O(1)
  - Lookup: O(1)
  - Delete: O(1)

Complexity (Worst - many collisions):
  - All operations: O(n)
```

### Python Built-in Hash Structures
```python
# dict - key-value pairs, O(1) average
hash_map = {}
hash_map['key'] = 'value'
print(hash_map.get('key', 'default'))

# set - unique elements, O(1) average
hash_set = set()
hash_set.add(element)
print(element in hash_set)

# defaultdict - auto-initialize missing keys
from collections import defaultdict
freq = defaultdict(int)
freq['a'] += 1

# Counter - frequency counting
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'a'])
print(counts.most_common(2))  # [('a', 3), ('b', 1)]

# OrderedDict - maintains insertion order
from collections import OrderedDict
ordered = OrderedDict()
ordered['first'] = 1
ordered.move_to_end('first')  # Move to end
ordered.popitem(last=False)   # Pop first item
```

## 🔄 Common Patterns

### Two Sum Pattern
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two indices that sum to target"""
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
```

### Frequency Counting
```python
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Find k most frequent elements"""
    counts = Counter(nums)
    return [num for num, _ in counts.most_common(k)]

# Bucket sort approach for O(n) time
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result
```

### Group Anagrams
```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings that are anagrams of each other"""
    groups = defaultdict(list)

    for s in strs:
        # Key: sorted characters (immutable tuple)
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())

# Alternative: character count as key
def group_anagrams_count(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)

    return list(groups.values())
```

### LRU Cache
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### Subarray Sum Equals K
```python
def subarray_sum(nums: list[int], k: int) -> int:
    """Count subarrays with sum equal to k"""
    count = 0
    prefix_sum = 0
    prefix_counts = {0: 1}  # Handle sum starting from index 0

    for num in nums:
        prefix_sum += num

        # If (prefix_sum - k) exists, there's a subarray with sum k
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]

        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return count
```

## 📚 Problem Catalog (35+)

### Easy (Foundation)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Two Sum | Hash Lookup | O(n) | O(n) |
| Contains Duplicate | Hash Set | O(n) | O(n) |
| Valid Anagram | Frequency Count | O(n) | O(1) |
| Happy Number | Cycle Detection | O(log n) | O(log n) |
| Isomorphic Strings | Bidirectional Map | O(n) | O(1) |

### Medium (Core)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Group Anagrams | Hash Grouping | O(n·k log k) | O(n·k) |
| LRU Cache | OrderedDict | O(1) | O(capacity) |
| Subarray Sum Equals K | Prefix Sum + Hash | O(n) | O(n) |
| Longest Consecutive Sequence | Hash Set | O(n) | O(n) |
| Find All Duplicates | Index as Hash | O(n) | O(1) |

### Hard (Expert)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| All O(1) Data Structure | Hash + DLL | O(1) all ops | O(n) |
| LFU Cache | Hash + DLL + FreqMap | O(1) all ops | O(capacity) |
| Substring Concatenation | Rolling Hash | O(n·m) | O(m) |
| Max Points on Line | Slope Hash | O(n²) | O(n) |

## 🧠 Advanced Patterns

### Longest Consecutive Sequence
```python
def longest_consecutive(nums: list[int]) -> int:
    """Find length of longest consecutive sequence"""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from sequence beginning
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
```

### Find All Duplicates (O(1) Space)
```python
def find_duplicates(nums: list[int]) -> list[int]:
    """Find duplicates using index as hash (values 1 to n)"""
    result = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]

    return result
```

### Custom Hash for Tuples
```python
def custom_hash_example():
    """Hash composite keys"""
    # Tuple as key (immutable)
    grid_visited = {}
    grid_visited[(0, 0)] = True
    grid_visited[(row, col, direction)] = True

    # Frozenset as key for unordered collections
    from collections import defaultdict
    group_by_set = defaultdict(list)
    for item in items:
        key = frozenset(item.properties)
        group_by_set[key].append(item)
```

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| TypeError: unhashable type | Using list as key | Convert to tuple |
| KeyError | Missing key access | Use `.get()` or `defaultdict` |
| Wrong frequency count | Not initializing | Use `Counter` or `defaultdict(int)` |
| Memory exceeded | Storing full objects | Store indices or hashes only |
| Hash collision | Poor hash function | Use built-in hash, avoid custom |

### Debug Checklist
```
□ Key type is hashable?
□ Using get() with default for missing keys?
□ Updating hash table in correct order?
□ Handling empty input?
□ Collision handling needed?
□ Memory efficient (store minimal)?
```

### Log Interpretation
```
[HSH-001] Unhashable type → Convert list to tuple
[HSH-002] Key collision → Check hash function
[HSH-003] Memory exceeded → Store references, not copies
[HSH-004] Wrong lookup → Verify key format matches
```

## 🛡️ Recovery Procedures

**If lookup fails unexpectedly:**
1. Print the key being looked up
2. Print all keys in hash table
3. Check for type mismatch (str vs int)
4. Verify key construction is consistent

**If memory exceeded:**
1. Store indices instead of full objects
2. Use hash of key instead of full key
3. Clear hash table after processing batches

## 🎓 Learning Path

```
Week 1: Hash Fundamentals
├── dict, set, Counter, defaultdict
├── Two Sum and frequency patterns
└── Practice: 10 Easy problems

Week 2: Advanced Patterns
├── Prefix sum + hash
├── Grouping and anagram problems
└── Practice: 10 Medium problems

Week 3: Complex Structures
├── LRU/LFU Cache
├── Custom hash functions
└── Practice: 5 Hard problems
```

## 💡 Interview Tips

1. **Default to hash map**: Many O(n²) become O(n) with hash
2. **Know your collections**: Counter, defaultdict, OrderedDict
3. **Immutable keys only**: Use tuples, frozensets for composite keys
4. **Consider memory**: Store minimal info (indices, counts)
5. **Edge cases**: Empty input, all duplicates, no matches

## 📊 Quick Reference Card

```
When to Use Hash:
  - O(1) lookup needed
  - Frequency counting
  - Duplicate detection
  - Grouping by property
  - Cache implementation

Python Collections:
  - dict: key-value store
  - set: unique elements
  - Counter: frequency counts
  - defaultdict: auto-initialize
  - OrderedDict: insertion order

Common Patterns:
  - Two Sum: complement lookup
  - Anagrams: sorted tuple as key
  - Subarray sum: prefix sum + count
  - Consecutive: set + boundary check
  - LRU: OrderedDict or DLL + hash
```

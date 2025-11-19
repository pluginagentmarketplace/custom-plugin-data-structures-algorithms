---
description: Master hash tables, sets, and hash-based data structures for fast lookups and duplicate detection. Covers collision handling, hash functions, and their applications.
capabilities: ["Hash Maps", "Hash Sets", "Collision Handling", "Frequency Counting", "Duplicate Detection", "Group Anagrams", "LRU Cache", "Two-Pass Solutions"]
---

# Hash Tables & Sets Agent

Expert in hash-based data structures for efficient lookups, insertions, and deletions.

## Core Concepts

### Hash Table Basics
- **Hash Function**: Maps keys to indices
- **Load Factor**: Elements / table size
- **Collision**: Multiple keys map to same index
- **Time Complexity**: O(1) average, O(n) worst case

### Collision Handling

**Chaining**
- Linked list at each bucket
- Handles high load factors well
- Extra memory for pointers

**Open Addressing**
- Linear probing, quadratic probing, double hashing
- All data in single array
- Sensitive to load factor

### Hash Table vs Set vs Map
- **Hash Table/Map**: Key-value pairs
- **Hash Set**: Unique elements only
- **Unordered Map/Set**: No order guarantee
- **Ordered Map/Set**: Maintains insertion/sorted order

## Common Applications

**Frequency Counting**
- Count occurrences of elements
- Find majority element
- Top K frequent elements

**Duplicate Detection**
- Find duplicates/unique elements
- Contains duplicate
- Find missing/duplicate numbers

**Grouping**
- Group anagrams
- Group shifts
- Group words that are isomorphic

**Two-Pass Solutions**
- First pass: Store in hash map/set
- Second pass: Check conditions
- Solves many problems elegantly

## Common Problems

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Happy Number
- Isomorphic Strings
- Word Pattern
- First Unique Character
- LRU Cache
- Intersection and Union
- Majority Element (hash variant)

## Learning Path

### Beginner Problems (Easy)
- Contains Duplicate
- Valid Anagram
- Two Sum
- Happy Number
- Isomorphic Strings

### Intermediate Problems (Medium)
- Group Anagrams
- First Unique Character in String
- LRU Cache
- Majority Element II
- Find All Duplicates in Array

### Advanced Problems (Hard)
- All O(1) Data Structure
- Max Points on a Line
- Substring with Concatenation of All Words
- Fraction to Recurring Decimal

## Advanced Data Structures

**LRU Cache Template**
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

**Frequency Map with Max Tracking**
```python
class FrequencyMap:
    def __init__(self):
        self.key_freq = {}
        self.freq_keys = {}
        self.min_freq = 0

    def inc(self, key):
        if key in self.key_freq:
            freq = self.key_freq[key]
            self.freq_keys[freq].remove(key)
            if not self.freq_keys[freq]:
                del self.freq_keys[freq]

        new_freq = self.key_freq.get(key, 0) + 1
        self.key_freq[key] = new_freq

        if new_freq not in self.freq_keys:
            self.freq_keys[new_freq] = []
        self.freq_keys[new_freq].append(key)
        self.min_freq = min(self.min_freq, new_freq)
```

## Hash Function Design

**Good Hash Function Properties**:
- Distributes keys uniformly
- Deterministic (same input → same output)
- Fast to compute
- Minimizes collisions

**Common Approaches**:
- Division method: h(k) = k mod m
- Multiplication method: h(k) = floor(m(k*A mod 1))
- Universal hashing for average-case guarantees

## Interview Tips
- Use hash map/set for O(1) lookups
- Consider frequency counting first
- Be aware of hash collisions in interviews
- Implement simple hash table from scratch if asked
- Know built-in data structures well
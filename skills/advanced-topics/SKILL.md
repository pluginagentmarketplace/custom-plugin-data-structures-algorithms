---
name: advanced-topics
description: Master advanced algorithmic techniques including hashing, bit manipulation, advanced data structures, and system design patterns. Use for competitive programming and production systems.
---

# Advanced Topics & System Design

## Quick Start

These techniques optimize solutions beyond basic algorithms.

## Hashing Fundamentals

### Hash Function Design
```python
def simple_hash(key, table_size):
    """Simple hash function for strings"""
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % table_size
    return hash_value

# Properties:
# - Deterministic: same input → same hash
# - Uniform distribution: minimizes collisions
# - Fast computation: O(k) where k = key length
```

### Collision Handling

#### Chaining
```python
class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """O(1) average"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        """O(1) average, O(n) worst"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```

#### Open Addressing (Linear Probing)
```python
class HashTableOpenAddressing:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size
        self.load_factor = 0.75

    def insert(self, key, value):
        if self._load() > self.load_factor:
            self._resize()

        index = hash(key) % self.size
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def _load(self):
        """Calculate load factor"""
        return sum(1 for x in self.table if x is not None) / self.size

    def _resize(self):
        """Rehash when load factor exceeds threshold"""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        for pair in old_table:
            if pair:
                self.insert(pair[0], pair[1])
```

### Common Applications
- **Hash Set**: O(1) duplicate detection
- **Hash Map**: Key-value storage
- **Counting Frequencies**: Hash map for character/number counts
- **Anagram Detection**: Sort and compare or use hash maps

## Bit Manipulation

### Fundamental Operations
```python
# AND: Both bits must be 1
a & b           # Example: 5 & 3 = 0101 & 0011 = 0001 = 1

# OR: At least one bit is 1
a | b           # Example: 5 | 3 = 0101 | 0011 = 0111 = 7

# XOR: Bits must be different
a ^ b           # Example: 5 ^ 3 = 0101 ^ 0011 = 0110 = 6

# NOT: Flip all bits
~a              # Example: ~5 = ~0101 = 1010 (in 4-bit)

# Left shift: Multiply by 2^n
a << n          # Example: 5 << 1 = 0101 << 1 = 1010 = 10

# Right shift: Divide by 2^n
a >> n          # Example: 5 >> 1 = 0101 >> 1 = 0010 = 2
```

### Useful Bit Tricks
```python
# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Toggle bit at position i
n ^= (1 << i)

# Set bit at position i
n |= (1 << i)

# Clear bit at position i
n &= ~(1 << i)

# Check if bit i is set
(n >> i) & 1 == 1

# Count set bits (Brian Kernighan)
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove rightmost set bit
        count += 1
    return count

# Single number (XOR finds unpaired element)
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Bit Manipulation Problems
- Single number in array (XOR properties)
- Power of 2 checking
- Hamming distance (count differing bits)
- Binary representation manipulation

## Advanced Data Structures

### Union-Find (Disjoint Set Union)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression: O(α(n)) amortized"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union with rank: O(α(n)) amortized"""
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def connected(self, x, y):
        """Check if connected"""
        return self.find(x) == self.find(y)
```

**Applications**: MST, cycle detection, grouping

### Trie (Prefix Tree)
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """O(m) where m = word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Find exact word: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        """Find words with prefix: O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**Applications**: Autocomplete, spell check, IP routing

### Segment Tree
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """Build tree: O(n)"""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, node, start, end, idx, val):
        """Update point: O(log n)"""
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node+1, start, mid, idx, val)
            else:
                self.update(2*node+2, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, start, end, l, r):
        """Range query: O(log n)"""
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(2*node+1, start, mid, l, r) +
                self.query(2*node+2, mid+1, end, l, r))
```

## System Design Patterns

### Caching Strategy
```python
from collections import OrderedDict

class LRUCache:
    """Least Recently Used Cache"""
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """O(1)"""
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """O(1)"""
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### Bloom Filter
```python
from hashlib import md5, sha1, sha256

class BloomFilter:
    """Fast membership testing, no false negatives"""
    def __init__(self, size, hash_functions=3):
        self.size = size
        self.bits = [False] * size
        self.hash_functions = [hash(i) for i in range(hash_functions)]

    def add(self, item):
        """Add item"""
        for i, h in enumerate(self.hash_functions):
            index = hash((item, i)) % self.size
            self.bits[index] = True

    def contains(self, item):
        """Check membership: O(k) where k = hash functions"""
        for i, h in enumerate(self.hash_functions):
            index = hash((item, i)) % self.size
            if not self.bits[index]:
                return False
        return True
```

## String Algorithms

### KMP (Knuth-Morris-Pratt)
```python
def kmp_search(text, pattern):
    """Find pattern in text: O(n + m)"""
    # Build failure function
    m = len(pattern)
    fail = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        fail[i] = j

    # Search
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1
```

## Modular Arithmetic

```python
# Modular multiplication to prevent overflow
result = (a * b) % MOD

# Modular exponentiation
def power_mod(base, exp, mod):
    """Fast exponentiation: O(log exp)"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Extended GCD for solving ax + by = gcd(a,b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
```

## Key Takeaways

✓ Hashing for O(1) lookups
✓ Bit manipulation for low-level optimization
✓ Union-Find for connectivity problems
✓ Tries for string pattern problems
✓ Segment Trees for range queries
✓ LRU Cache for bounded memory caching
✓ KMP for efficient string searching
✓ Modular arithmetic for number problems

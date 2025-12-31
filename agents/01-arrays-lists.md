---
name: 01-arrays-lists
description: Master array and list data structures with advanced techniques including two-pointer, sliding window, prefix sums, and optimization strategies. Essential foundation for interview success with 50+ real problems.
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - arrays
  - linked-lists
triggers:
  - "dsa arrays"
  - "dsa"
  - "leetcode"
capabilities:
  - Array Manipulation
  - Two Pointer Technique
  - Sliding Window Pattern
  - Prefix Sum Optimization
  - In-Place Algorithms
  - Subarray Problems
  - Space-Time Tradeoffs
  - Edge Case Handling

# Production-Grade Specifications (2025)
input_schema:
  type: object
  required: [problem_type]
  properties:
    problem_type:
      type: string
      enum: [traversal, search, manipulation, optimization, pattern]
    difficulty:
      type: string
      enum: [easy, medium, hard]
    constraints:
      type: object
      properties:
        max_array_size: { type: integer, default: 100000 }
        element_range: { type: array, items: { type: integer } }
        allow_duplicates: { type: boolean, default: true }
        sorted: { type: boolean, default: false }

output_schema:
  type: object
  properties:
    solution:
      type: object
      properties:
        approach: { type: string }
        code: { type: string }
        time_complexity: { type: string }
        space_complexity: { type: string }
    explanation:
      type: string
    edge_cases:
      type: array
      items: { type: string }
    follow_up:
      type: array
      items: { type: string }

error_handling:
  retry_count: 3
  backoff_strategy: exponential
  backoff_base_ms: 100
  max_backoff_ms: 5000
  recoverable_errors:
    - context_overflow
    - partial_response
    - ambiguous_input

fallback_strategy:
  primary: detailed_walkthrough
  secondary: step_by_step_hints
  tertiary: reference_to_skill

token_budget:
  max_context: 8000
  response_reserve: 2000
  skill_allocation: 1500

observability:
  logging: true
  metrics: true
  trace_id_prefix: "ARR"

prerequisites:
  required: []
  recommended:
    - basic-programming
    - time-complexity-basics

bonded_skills:
  primary: array-techniques
  secondary:
    - sliding-window-pattern
    - prefix-sum-technique
---

# 📊 Arrays & Lists Master Agent

**The Foundation of All Data Structures** — Production-Grade v2.0

Arrays are the foundation of every software engineer's toolkit. Master them, and you master 30% of all interview problems.

## 🎯 Core Competencies

### Array Operations & Complexity
| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| Access | O(1) | O(1) | Direct index |
| Search | O(n) | O(n) | Linear scan |
| Insert (end) | O(1)* | O(n) | *Amortized |
| Insert (middle) | O(n) | O(n) | Shift required |
| Delete | O(n) | O(n) | Shift required |

### Key Techniques

**1. Two Pointers** — Efficiently traverse paired elements
```python
# Pattern: Opposite direction (converging)
def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []  # Not found
```

**2. Sliding Window** — Contiguous subarray problems
```python
# Pattern: Variable-size window
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

**3. Prefix Sums** — O(1) range queries
```python
# Pattern: Precompute cumulative sums
class PrefixSum:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

## 📚 Problem Catalog (50+)

### Easy (Foundation)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Two Sum | Hash Map | O(n) | O(n) |
| Best Time to Buy Stock | Single Pass | O(n) | O(1) |
| Contains Duplicate | Hash Set | O(n) | O(n) |
| Merge Sorted Array | Two Pointers | O(m+n) | O(1) |
| Remove Duplicates | Fast/Slow Pointer | O(n) | O(1) |

### Medium (Core)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| 3Sum | Two Pointers + Sort | O(n²) | O(1) |
| Container With Most Water | Two Pointers | O(n) | O(1) |
| Product Except Self | Prefix/Suffix | O(n) | O(1) |
| Subarray Sum Equals K | Prefix Sum + Hash | O(n) | O(n) |
| Longest Substring No Repeat | Sliding Window | O(n) | O(min(m,n)) |

### Hard (Expert)
| Problem | Pattern | Time | Space |
|---------|---------|------|-------|
| Trapping Rain Water | Two Pointers/Stack | O(n) | O(1) |
| Median of Two Sorted Arrays | Binary Search | O(log(m+n)) | O(1) |
| Sliding Window Maximum | Monotonic Deque | O(n) | O(k) |
| First Missing Positive | Index as Hash | O(n) | O(1) |

## 🔧 Troubleshooting Guide

### Common Failure Modes

| Error | Root Cause | Solution |
|-------|------------|----------|
| Index Out of Bounds | Off-by-one in loop bounds | Use `len(arr) - 1` for last valid index |
| Infinite Loop | Window never shrinks | Ensure `left` increments in while loop |
| Wrong Answer on Empty Array | Missing edge case | Add `if not arr: return default` |
| TLE (Time Limit Exceeded) | O(n²) when O(n) possible | Consider hash map or two pointers |
| Memory Limit Exceeded | Creating unnecessary copies | Use in-place modification |

### Debug Checklist
```
□ Edge cases handled? (empty, single element, all same)
□ Pointer bounds checked? (left < right, i < len)
□ Integer overflow possible? (use // for division)
□ Sorted array assumption valid?
□ Duplicate elements considered?
□ Negative numbers handled?
```

### Log Interpretation
```
[ARR-001] Input validation failed → Check constraints
[ARR-002] Pattern mismatch → Review problem type
[ARR-003] Complexity exceeded → Optimize approach
[ARR-004] Edge case triggered → Handle boundary
```

## 🛡️ Recovery Procedures

**If solution times out:**
1. Analyze current complexity
2. Identify nested loops
3. Consider hash map for O(1) lookups
4. Apply two-pointer if sorted
5. Use prefix sum for range queries

**If solution gives wrong answer:**
1. Trace through small example manually
2. Check array modification side effects
3. Verify loop invariants
4. Test edge cases explicitly

## 🎓 Learning Path

```
Week 1: Basic Operations
├── Array traversal patterns
├── Two-pointer fundamentals
└── Practice: 10 Easy problems

Week 2: Pattern Mastery
├── Sliding window variations
├── Prefix sum applications
└── Practice: 15 Medium problems

Week 3: Advanced Techniques
├── In-place algorithms
├── Complex optimizations
└── Practice: 5 Hard problems
```

## 💡 Interview Tips

1. **Clarify constraints first**: Negative numbers? Duplicates? Sorted?
2. **State complexity before coding**: "This will be O(n) time, O(1) space"
3. **Handle edge cases explicitly**: Empty array, single element
4. **Optimize incrementally**: Brute force → better → optimal
5. **Test with examples**: Walk through your code with input

## 📊 Quick Reference Card

```
Two Pointers:
  - Opposite: left=0, right=n-1, converge
  - Same direction: slow/fast, remove in-place

Sliding Window:
  - Fixed: sum of k elements
  - Variable: smallest subarray with sum ≥ target

Prefix Sum:
  - Build: prefix[i] = prefix[i-1] + arr[i]
  - Query: sum(i,j) = prefix[j+1] - prefix[i]

Common Patterns:
  - Kadane's: max subarray (DP approach)
  - Dutch Flag: 3-way partition
  - Cyclic Sort: find missing/duplicate
```

---
name: bit-manipulation
description: Bit manipulation tricks and techniques for solving problems efficiently using binary operations and XOR properties.
sasmp_version: "1.3.0"
bonded_agent: 01-arrays-lists
bond_type: PRIMARY_BOND
---

# Bit Manipulation Skill

## Basic Bit Operations
```python
# Set i-th bit
def setBit(num, i):
    return num | (1 << i)

# Clear i-th bit
def clearBit(num, i):
    return num & ~(1 << i)

# Toggle i-th bit
def toggleBit(num, i):
    return num ^ (1 << i)

# Check if i-th bit is set
def isBitSet(num, i):
    return (num & (1 << i)) != 0

# Check if power of 2
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Get rightmost set bit
def getRightmostBit(num):
    return num & (-num)

# Remove rightmost set bit
def removeRightmostBit(num):
    return num & (num - 1)
```

## Single Number Problems (XOR)
```python
# Find single number appearing once, others twice
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Find two single numbers
def findTwoSingle(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Get rightmost set bit
    rightmost = xor_all & (-xor_all)

    num1 = num2 = 0
    for num in nums:
        if num & rightmost:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]
```

## Hamming Distance
```python
def hammingDistance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

# Using Brian Kernighan's algorithm
def hammingDistanceOpt(x, y):
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count
```

## Subset Generation
```python
# Generate all subsets using bits
def subsetsWithBits(nums):
    result = []
    n = len(nums)

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result

# Count number of 1 bits
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Or use built-in
def countSetBitsBuiltin(n):
    return bin(n).count('1')
```
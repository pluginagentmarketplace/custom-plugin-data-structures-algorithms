# Bit Manipulation Guide

## Common Operations
```python
# Check if bit i is set
(n >> i) & 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Toggle bit i
n ^ (1 << i)
```

## Tricks
- **Power of 2**: `n & (n-1) == 0`
- **Count ones**: Brian Kernighan's algorithm
- **Single number**: XOR all elements
- **Even/Odd**: `n & 1`

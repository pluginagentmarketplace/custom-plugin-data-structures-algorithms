---
name: bit-manipulation
description: Master bit operations. AND, OR, XOR, shifts. Tricks for common problems. Essential for system design and optimization.
---

# Bit Manipulation

## Basic Operations
- AND (&): Both 1
- OR (|): At least one 1
- XOR (^): Different bits
- NOT (~): Flip all
- Left shift (<<): Multiply by 2^n
- Right shift (>>): Divide by 2^n

## Useful Tricks
- Check power of 2: n & (n-1) == 0
- Toggle bit i: n ^= (1 << i)
- Set bit i: n |= (1 << i)
- Clear bit i: n &= ~(1 << i)
- Check bit i: (n >> i) & 1

## XOR Properties
- a ^ a = 0
- a ^ 0 = a
- XOR commutative: a ^ b = b ^ a
- Find single unpaired element: XOR all

## Common Problems
- Single number (XOR solution)
- Power of 2
- Hamming distance
- Binary representation

## Interview Tip
Bit manipulation often gives O(1) space solution

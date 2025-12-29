# Backtracking Guide

## Template
```python
def backtrack(path, choices):
    if is_goal(path):
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(choice):
            path.append(choice)      # Choose
            backtrack(path, ...)     # Explore
            path.pop()               # Unchoose
```

## Problems
- Permutations: All orderings
- Combinations: Select k from n
- Subsets: All possible subsets
- N-Queens: Place n queens safely

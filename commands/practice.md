# /practice

Get targeted practice problems and coding challenges.

## Description

This command provides carefully selected practice problems based on your focus area and difficulty level.

## How to Use

Use `/practice` followed by options:

### By Agent
```
/practice agent:foundations
/practice agent:linear-structures
/practice agent:nonlinear-structures
/practice agent:searching-sorting
/practice agent:dynamic-programming
/practice agent:graph-algorithms
/practice agent:advanced-topics
```

### By Difficulty
```
/practice level:easy          # 15-20 min each
/practice level:medium        # 30-45 min each
/practice level:hard          # 60+ min each
```

### By Problem Type
```
/practice type:tree
/practice type:array
/practice type:string
/practice type:graph
/practice type:dynamic-programming
/practice type:bit-manipulation
/practice type:design
```

### Combined
```
/practice agent:dynamic-programming level:medium
/practice type:graph level:hard
```

## Problem Categories

### By Difficulty

#### Easy (Warm-up)
- Basic operations on data structures
- Simple problem variations
- Implementation practice
- ~15-20 minutes each
- Example: "Two Sum", "Reverse String"

#### Medium (Core)
- Multi-concept problems
- Optimization required
- ~30-45 minutes each
- Example: "LCA of Binary Tree", "Coin Change"

#### Hard (Mastery)
- Complex problem-solving
- Multiple techniques combined
- 60+ minutes
- Example: "Serialize/Deserialize BST", "Russian Doll Envelopes"

### By Type

#### Array/String Problems
- Sorting, searching, manipulation
- Two-pointer, sliding window
- Prefix/suffix patterns
- Range queries

#### Tree Problems
- Traversals, BST operations
- Tree modification
- LCA, diameter, balance
- Serialization

#### Graph Problems
- Traversal, connectivity
- Shortest path, MST
- Cycle detection
- Topological ordering

#### Dynamic Programming
- Sequence DP
- Grid DP
- String DP
- Optimization problems

#### Bit Manipulation
- Bit operations
- Number problems
- XOR patterns
- Power of 2 operations

#### Design Problems
- Data structure design
- System patterns
- Optimization
- Real-world scenarios

## Practice Structure

1. **Problem Statement**: Clear problem description
2. **Constraints**: Input ranges and requirements
3. **Examples**: Sample input/output
4. **Hints**: Nudges without spoilers
5. **Time Complexity Goal**: What to aim for
6. **Solution**: Detailed explanation

## Recommended Practice Schedule

### Daily Practice (1 hour)
- 1 Easy problem (15 min)
- 1 Medium problem (35 min)
- Review one concept (10 min)

### Weekly Goals
- Mon-Wed: One agent deep dive
- Thu: Mixed problems
- Fri-Sat: Hard problems
- Sun: Review and reflect

### Interview Prep (8 weeks)
- Weeks 1-2: Foundations (daily easy)
- Weeks 3-4: Linear + Searching (2 medium/day)
- Weeks 5-6: Trees + Graphs (1 hard/day)
- Weeks 7-8: Mock interviews

## Tips for Effective Practice

### Before Coding
- [ ] Read problem carefully
- [ ] Identify patterns
- [ ] Plan approach on paper
- [ ] Estimate complexity

### While Coding
- [ ] Write clean code
- [ ] Handle edge cases
- [ ] Add comments
- [ ] Test with examples

### After Coding
- [ ] Verify correctness
- [ ] Calculate complexity
- [ ] Optimize if possible
- [ ] Study similar problems

## Tracking Progress

Keep a problem journal:
- Problem name and date
- Difficulty (easy/medium/hard)
- Time spent
- Approach used
- Complexity achieved
- Notes for future

## Problem Sources

- LeetCode (Free tier and Premium)
- HackerRank Algorithm challenges
- CodeSignal for assessments
- Company-specific OA platforms
- GitHub problem repositories

## Next Steps

1. **Choose** an agent and difficulty
2. **Solve** the problem independently
3. **Review** solutions and explanations
4. **Compare** your approach with optimal
5. **Repeat** with harder problems

## Example Workflow

```
/practice agent:dynamic-programming level:medium
→ Receive 3-5 DP problems
→ Solve first problem
→ Ask Claude to review approach
→ Compare complexity
→ Move to next problem
→ /practice agent:graph-algorithms level:hard
→ Step up difficulty
```

## Streak Challenge

Try to maintain a practice streak:
- Easy: 15 min/day (easy 7-day streak)
- Medium: 30 min/day (good 14-day streak)
- Hard: 60 min/day (ambitious 21-day streak)

Track and celebrate your progress!

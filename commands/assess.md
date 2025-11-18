# /assess - Knowledge Assessment

Test your understanding of Data Structures & Algorithms.

## Usage

```
/assess
```

or for specific topic:

```
/assess [topic]
```

## Assessment Levels

### 🟢 Beginner Assessment (15-20 minutes)
Test fundamental understanding.

**Topics Covered:**
- Big-O notation basics
- Array vs linked list use cases
- Tree traversal methods
- BFS vs DFS concepts
- When to use DP vs greedy
- Basic sorting algorithm properties

**Questions:** 10-15 multiple choice + 2-3 coding

**Passing Score:** 70%+

**If you pass:** Continue to intermediate

**If you don't:** Review fundamentals, then reassess

---

### 🟡 Intermediate Assessment (25-30 minutes)
Evaluate practical problem-solving skills.

**Topics Covered:**
- Complexity analysis of code
- Two-pointer techniques
- Tree problem solving
- Graph traversal applications
- Basic DP state definition
- Sorting algorithm selection

**Questions:** 15-20 multiple choice + 5-8 coding

**Passing Score:** 75%+

**If you pass:** Move to advanced

**If you don't:** Study intermediate materials more

---

### 🔴 Advanced Assessment (40-45 minutes)
Interview-level problem solving.

**Topics Covered:**
- Complex algorithm analysis
- Advanced tree problems
- Graph algorithms integration
- DP pattern recognition
- Optimization techniques
- System design thinking

**Questions:** 20-25 multiple choice + 10-15 coding

**Passing Score:** 80%+

**If you pass:** Interview-ready!

**If you don't:** Focus on weak areas

---

## Assessment Topics

Choose specific topics to assess:

### Complexity Analysis
- Big-O notation
- Time/space complexity
- Amortized analysis
- Master theorem

### Linear Data Structures
- Arrays and linked lists
- Stacks and queues
- Two-pointer techniques
- Sliding window

### Tree Structures
- Binary trees
- BST operations
- Tree traversals
- Heaps and priority queues

### Graph Algorithms
- BFS/DFS
- Shortest paths
- Minimum spanning trees
- Topological sort

### Dynamic Programming
- State definition
- Recurrence relations
- DP patterns
- Optimization

### Sorting & Searching
- Sorting algorithms
- Binary search
- Selection algorithms
- Algorithm selection

### Advanced Techniques
- Greedy algorithms
- Backtracking
- Bit manipulation
- Union-find

---

## Assessment Format

### Multiple Choice (40%)
Quick concept validation.

**Example:**
```
Q: What's the time complexity of binary search?
A) O(1)
B) O(log n)  ← Correct
C) O(n)
D) O(n²)
```

### Coding Problems (60%)
Real problem-solving.

**Example:**
```
Problem: Two Sum
Given array and target, find two numbers that sum to target
Return indices

Input: [2, 7, 11, 15], 9
Output: [0, 1]

Constraints: O(n) time, O(n) space

Time: 10-15 minutes
Difficulty: Easy
```

---

## Scoring & Feedback

### Your Assessment Report Includes:

**Score Breakdown:**
- Overall score (0-100)
- Topic-wise breakdown
- Strengths and weaknesses
- Specific areas to improve

**Detailed Feedback:**
- Explanation of correct answers
- Why other options were wrong
- Common mistakes to avoid
- Resources for improvement

**Recommendations:**
- Which topics to focus on
- Suggested problems to solve
- Time to spend on each area
- Next assessment time

---

## Sample Questions

### Easy (Beginner)

**Q1: Big-O Basics**
```
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

Time complexity?
A) O(1)
B) O(log n)
C) O(n)  ← Correct
D) O(n²)
```

**Q2: Linked List Use Case**
```
When would you choose linked list over array?
A) Need random access
B) Need to frequently insert at head
C) Want cache efficiency
D) Need to access elements by index

Answer: B
Linked list is O(1) at head, array is O(n)
```

### Medium (Intermediate)

**Q3: Problem Solving**
```
Problem: Longest Substring Without Repeating
Given string, find length of longest substring without repeating
Time: O(n), Space: O(min(n, charset))

Which technique?
A) Brute force
B) Sliding window  ← Correct
C) Dynamic programming
D) Binary search

Why: Maintain window of non-repeating chars
```

### Hard (Advanced)

**Q4: System Design**
```
Design auto-complete for 1M queries
Choose data structure:
A) Sorted array
B) Hash map
C) Trie  ← Correct
D) Segment tree

Why: O(m) search (m=prefix length), not O(n)
```

---

## Assessment Schedule

**Recommended Timeline:**

```
Week 1: Beginner Assessment
↓
Weeks 2-3: Intermediate Assessment
↓
Weeks 4-6: Topic-specific Assessments
↓
Week 7: Advanced Assessment
↓
Interview-Ready Assessment
```

---

## Using Assessment Results

### If You Score 80%+
✅ **Great!** You're ready for:
- Next difficulty level
- Interview preparation
- Competitive programming
- System design problems

### If You Score 60-79%
⚠️ **Good Progress**
- Review topics you got wrong
- Solve more practice problems
- Reassess same topic
- Move to next topic

### If You Score <60%
❌ **Need More Practice**
- Review fundamentals
- Work through examples step-by-step
- Solve 20+ basic problems
- Reassess this topic

---

## Assessment Features

✅ **Instant Feedback**
- Immediate score and explanations
- Detailed answer breakdown
- Learning resources linked

✅ **Adaptive Difficulty**
- Questions adjust to your level
- Skipped topics if mastered
- Extra practice for weak areas

✅ **Progress Tracking**
- Historical scores
- Improvement over time
- Weakness identification
- Strength reinforcement

✅ **Interview Simulation**
- Timed assessments
- Real problem formats
- Interview-style feedback
- Mock interview option

---

## Mock Interview Mode

After passing advanced assessment:

```
/assess interview-mock
```

This provides:
- 3-4 real interview problems
- 45 minute timer (like real interview)
- No access to external resources
- Realistic feedback
- Interview tips at end

---

## Retaking Assessments

**You can retake:**
- Same topic after more practice
- Different difficulty level
- Full assessment for progress tracking

**Recommended wait time:**
- Easy to Medium: 1 week of practice
- Medium to Hard: 2 weeks of practice
- Same difficulty: 2-3 days

---

## Assessment Tips

✅ **Before Assessment:**
- Ensure no distractions
- Have paper for notes
- Have 30-50 minutes free
- Be honest with yourself

✅ **During Assessment:**
- Read questions carefully
- Think before answering
- Work through problems step-by-step
- Don't skip difficult ones

✅ **After Assessment:**
- Review incorrect answers
- Understand why you missed them
- Study recommended topics
- Schedule next assessment

---

## Get Started

Choose your assessment:

1. **Start with Beginner**
   ```
   /assess beginner
   ```

2. **Or pick a topic**
   ```
   /assess complexity
   /assess trees
   /assess dynamic-programming
   ```

3. **Or take Mock Interview**
   ```
   /assess interview-mock
   ```

---

**Ready to test your knowledge? Let's assess!**

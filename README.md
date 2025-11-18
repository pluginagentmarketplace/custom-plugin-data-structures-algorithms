# Data Structures & Algorithms Mastery Plugin

A comprehensive, professional-grade learning system for mastering Data Structures and Algorithms using Claude Code.

## 🎯 Overview

Master **Data Structures and Algorithms** with a structured, agent-based learning system. This plugin provides:

- **7 Specialized Agents** covering all DSA topics
- **7 Interactive Skills** with detailed examples and best practices
- **4 Powerful Commands** for learning, practice, and interview prep
- **1000+ Hours** of learning content
- **Real-world Applications** and system design patterns
- **Interview-Ready** preparation with company-specific guides

## ✨ Key Features

### 📚 Comprehensive Coverage

**Foundations & Complexity Analysis**
- Big O notation and asymptotic analysis
- Time/space complexity calculation
- Algorithm efficiency comparison

**Linear Data Structures**
- Arrays and strings
- Linked lists (all variations)
- Stacks and queues
- Two-pointer and sliding window techniques

**Non-Linear Data Structures**
- Binary trees and BSTs
- Balanced trees and heaps
- Tries for pattern matching
- Graph basics

**Searching & Sorting Algorithms**
- Linear and binary search
- Comparison-based sorts
- Non-comparison sorts (Counting, Radix)
- Advanced search optimization

**Dynamic Programming**
- Problem identification
- State definition and transitions
- Memoization vs tabulation
- Space optimization

**Graph Algorithms**
- Traversal (BFS, DFS)
- Shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning trees
- Topological sorting

**Advanced Topics & System Design**
- Hash table design
- Bit manipulation
- Advanced data structures
- Real-world optimization

### 🎓 Learning Paths

**By Experience Level**
- Beginner: New to DSA
- Intermediate: Familiar with basics
- Advanced: Ready for complex topics

**By Goal**
- Interview Preparation (targeted for FAANG)
- Competitive Programming (speed optimization)
- System Design (real-world applications)
- Comprehensive Mastery (deep understanding)

**By Timeline**
- Quick Path: 2-3 weeks
- Standard Path: 6-8 weeks
- Deep Dive: 12+ weeks

### 🚀 Commands

#### `/learn`
Start your personalized learning journey with guided path selection based on your level and goals.

#### `/explore-agent`
Discover all 7 specialized agents, their focus areas, and when to use them. Includes dependency recommendations.

#### `/practice`
Get targeted practice problems by:
- Agent/topic
- Difficulty level (Easy/Medium/Hard)
- Problem type (Array, Tree, Graph, DP, etc.)

#### `/interview-prep`
Prepare for technical interviews with:
- Company-specific guides (Google, Amazon, Meta, Microsoft)
- Interview type preparation (Phone screen, Onsite, Takehome)
- Time-based preparation plans (2-week to 12-week)
- Mock interview setup and feedback

## 🏗️ Plugin Structure

```
custom-plugin-data-structures-algorithms/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
│
├── agents/                      # 7 Specialized Agents
│   ├── 01-foundations-complexity.md
│   ├── 02-linear-data-structures.md
│   ├── 03-nonlinear-data-structures.md
│   ├── 04-searching-sorting.md
│   ├── 05-dynamic-programming.md
│   ├── 06-graph-algorithms.md
│   └── 07-advanced-topics.md
│
├── skills/                      # 7 Interactive Skills
│   ├── foundations/SKILL.md
│   ├── linear-structures/SKILL.md
│   ├── nonlinear-structures/SKILL.md
│   ├── searching-sorting/SKILL.md
│   ├── dynamic-programming/SKILL.md
│   ├── graph-algorithms/SKILL.md
│   └── advanced-topics/SKILL.md
│
├── commands/                    # 4 Slash Commands
│   ├── learn.md
│   ├── explore-agent.md
│   ├── practice.md
│   └── interview-prep.md
│
├── hooks/
│   └── hooks.json               # Automation and tracking
│
└── README.md                    # This file
```

## 🚀 Quick Start

### Installation

1. **Clone or Use Locally**
   ```bash
   # If you have the repo path
   /plugin-add ./custom-plugin-data-structures-algorithms

   # Or add to Claude Code marketplace
   /plugin-add @claude/data-structures-algorithms
   ```

2. **Start Learning**
   ```
   /learn
   ```

3. **Explore Agents**
   ```
   /explore-agent
   ```

4. **Practice Problems**
   ```
   /practice agent:foundations level:easy
   ```

5. **Prepare for Interviews**
   ```
   /interview-prep target:google timeline:8-weeks
   ```

## 📊 Content Breakdown

| Component | Count | Coverage |
|-----------|-------|----------|
| Agents | 7 | All major DSA topics |
| Skills | 7 | Interactive, example-rich |
| Commands | 4 | Learning, practice, interviews |
| Topics | 60+ | Comprehensive DSA |
| Algorithms | 100+ | All classic algorithms |
| Code Examples | 500+ | Real, working code |
| Practice Problems | 100+ | Curated, categorized |
| Time to Master | 1000+ hours | Comprehensive coverage |

## 🎓 Learning Approach

### Recommended Path

**Week 1-2: Foundations**
- Big O notation mastery
- Complexity analysis
- Algorithm efficiency concepts

**Week 3-4: Linear Structures**
- Arrays and strings
- Linked lists
- Stacks and queues

**Week 5-6: Searching & Non-Linear**
- Binary search variations
- Tree algorithms
- Sorting algorithms

**Week 7-8: Advanced**
- Dynamic programming
- Graph algorithms
- Advanced optimization

**Week 9-12: Interview Focus**
- Company-specific questions
- Mock interviews
- Final optimization

## ✅ Success Checklist

- [ ] Completed Foundations agent
- [ ] Solved 100+ problems
- [ ] Understand all concepts deeply
- [ ] Can explain solutions clearly
- [ ] Pass 3+ mock interviews
- [ ] Comfortable under time pressure
- [ ] Handle edge cases systematically
- [ ] Optimize for both time and space

## 🎓 Start Learning Now!

Choose your path:

```
/learn                          # Personalized learning journey
/explore-agent                  # Discover agents
/practice level:easy            # Start with easy problems
/interview-prep target:google   # Prepare for big tech
```

**Happy Learning!** 📚✨

Remember: Consistent daily practice is the key to mastery. Start with easy problems, understand the patterns, and gradually increase difficulty. You've got this!

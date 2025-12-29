<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Data+Structures+Algorithms+Assistant;7+Agents+%7C+8+Skills;Claude+Code+Plugin" alt="Data Structures Algorithms Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-7-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-8-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms)

---

### What is this?

> **Data Structures Algorithms Assistant** is a Claude Code plugin with **7 agents** and **8 skills** for data structures algorithms development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin add marketplace pluginagentmarketplace/custom-plugin-data-structures-algorithms

# Step 2️⃣ Install the plugin
/plugin install data-structures-algorithms-assistant@pluginagentmarketplace-data-structures-algorithms

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms.git
cd custom-plugin-data-structures-algorithms

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
data-structures-algorithms-assistant:02-trees-binary
data-structures-algorithms-assistant:07-greedy-advanced
data-structures-algorithms-assistant:01-arrays-lists
data-structures-algorithms-assistant:04-dynamic-programming
data-structures-algorithms-assistant:06-hash-tables
... and 2 more
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **7 Agents** | Specialized AI agents for data structures algorithms tasks |
| 🛠️ **8 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |

---

## 🤖 Agents

### 7 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **02-trees-binary** | Master tree data structures, including binary trees, BSTs, b |
| 2 | **07-greedy-advanced** | Master greedy algorithms and advanced techniques for optimiz |
| 3 | **01-arrays-lists** | Master array and list data structures with advanced techniqu |
| 4 | **04-dynamic-programming** | Master dynamic programming, the technique for solving optimi |
| 5 | **06-hash-tables** | Master hash tables, sets, and hash-based data structures for |
| 6 | **03-graphs** | Master graph data structures and algorithms, including repre |
| 7 | **05-sorting-searching** | Master sorting and searching algorithms, fundamental techniq |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `trees` | Master tree traversal techniques including DFS (inorder, pre | `Skill("data-structures-algorithms-assistant:trees")` |
| `backtracking` | Master backtracking technique with permutations, combination | `Skill("data-structures-algorithms-assistant:backtracking")` |
| `hashing` | Hash-based data structures and techniques including frequenc | `Skill("data-structures-algorithms-assistant:hashing")` |
| `bitmanip` | Bit manipulation tricks and techniques for solving problems  | `Skill("data-structures-algorithms-assistant:bitmanip")` |
| `arrays` | Master essential array techniques including two pointers, sl | `Skill("data-structures-algorithms-assistant:arrays")` |
| `sorting` | Complete sorting algorithm implementations including quick s | `Skill("data-structures-algorithms-assistant:sorting")` |
| `dp` | Master DP patterns with complete implementations for memoiza | `Skill("data-structures-algorithms-assistant:dp")` |
| `graphs` | Essential graph algorithms including DFS, BFS, Dijkstra shor | `Skill("data-structures-algorithms-assistant:graphs")` |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/complexity-analyzer` | Complexity Analyzer - Master Time & Space Complexity |
| `/interview-prep` | 🚀 Interview Mastery - Ace Your Coding Interview |
| `/difficulty-selector` | Difficulty Selector - Choose Your Challenge Level |
| `/problem-solver` | 🎯 Problem Solver - Master DSA Through Practice |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-data-structures-algorithms/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 7 agents
├── 📁 skills/              # 8 skills (Golden Format)
├── 📁 commands/            # 4 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Last Updated** | 2025-12-29 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 7 |
| **Skills** | 8 |
| **Commands** | 4 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>

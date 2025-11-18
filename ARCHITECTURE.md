# Plugin Architecture

## Overview

This Claude Code plugin implements a comprehensive DSA learning system with 7 specialized agents, interactive skills, and structured learning paths.

## Component Structure

### Plugin Manifest (.claude-plugin/plugin.json)

Central configuration file containing:
- Plugin metadata (name, version, description)
- 7 Agent definitions with file paths and descriptions
- 4 Command references
- 7 Skill definitions with directories
- Hook configurations
- MCP server definitions

### Agents (agents/)

**7 Markdown Files** - Each agent is a specialized markdown file with YAML frontmatter:

```yaml
---
description: Agent specialization
capabilities: [list of capabilities]
---

# Agent Name
[Detailed content about this agent's specialty]
```

**Agent Types:**
1. `complexity-analyst` - Complexity analysis and Big-O notation
2. `linear-structures-expert` - Arrays, linked lists, stacks, queues
3. `tree-structures-master` - All tree data structures
4. `graph-algorithms-guide` - Graph theory and algorithms
5. `dp-strategist` - Dynamic programming patterns
6. `sort-search-optimizer` - Sorting and searching algorithms
7. `advanced-techniques-guide` - Advanced problem-solving and interviews

**Load Mechanism:**
- Agents are loaded by Claude when:
  - User explicitly requests them via `/browse-agent`
  - Learning path recommends them
  - Relevant to user's current task

### Skills (skills/)

**7 Skill Directories** - Each contains SKILL.md with:

```markdown
---
name: skill-id
description: Skill description
---

# Skill Name
[Detailed skill content with code examples]
```

**Skill Organization:**
```
skills/
├── 01-complexity/SKILL.md
├── 02-linear-structures/SKILL.md
├── 03-tree-structures/SKILL.md
├── 04-graph-algorithms/SKILL.md
├── 05-dynamic-programming/SKILL.md
├── 06-sorting-searching/SKILL.md
└── 07-advanced-techniques/SKILL.md
```

**Load Mechanism:**
- Skills load when:
  - User mentions relevant keywords
  - Agent invokes related skill
  - Learning path explicitly includes it
  - User runs `/assess` or `/interview-prep`

### Commands (commands/)

**4 Markdown Files** - Slash commands for navigation:

1. `/learn` - Start learning journey
   - Assess user level
   - Create personalized path
   - Recommend first agent

2. `/browse-agent` - Explore all agents
   - List all 7 agents
   - Compare capabilities
   - Select specific agent

3. `/assess` - Knowledge assessment
   - Multiple difficulty levels
   - Topic-specific tests
   - Instant feedback

4. `/interview-prep` - Interview preparation
   - Company-specific tracks
   - Mock interviews
   - Problem collections

### Hooks (hooks/hooks.json)

**Automation Configuration** - Defines:

1. **Learning Progress Tracker** - Tracks completion
2. **Problem Validator** - Validates solutions
3. **Interview Simulator** - Real interview experience
4. **Assessment Tracker** - Score tracking
5. **Skill Progression** - Level progression
6. **Community Engagement** - Participation metrics

## Data Flow

### Learning Path Flow
```
/learn
  ↓
[Skill Assessment]
  ↓
[Personalized Path Creation]
  ↓
[Agent Recommendation]
  ↓
[Skill Module Loading]
  ↓
[Problem Practice]
  ↓
[Progress Tracking]
  ↓
[Next Agent Recommendation]
```

### Agent Usage Flow
```
User Query
  ↓
[Determine Relevant Agent]
  ↓
[Load Agent Markdown]
  ↓
[Parse YAML Frontmatter]
  ↓
[Display Agent Content]
  ↓
[Link to Related Skills]
  ↓
[Suggest Practice Problems]
```

### Skill Invocation Flow
```
Agent/User Reference
  ↓
[Skill Name Match]
  ↓
[Load SKILL.md]
  ↓
[Parse Code Examples]
  ↓
[Display Content]
  ↓
[Provide Quick Start]
  ↓
[Link to Problems]
```

## Content Organization

### By Difficulty Level
- **Beginner**: Complexity + Linear Structures
- **Intermediate**: Trees + Graphs + DP
- **Advanced**: Sorting + Advanced Techniques

### By Problem Solving Approach
- **Array/String**: Linear Structures
- **Tree**: Tree Master
- **Graph**: Graph Guide
- **Optimization**: DP Strategist
- **Pattern Recognition**: Advanced Techniques
- **Interview**: All agents + Interview Prep

### By Learning Style
- **Visual Learners**: Complexity tables, diagrams
- **Code Learners**: 70+ code examples
- **Problem Solvers**: 200+ practice problems
- **Interview Focused**: Mock interviews, company tracks

## Complexity Analysis

### Plugin Size
- **Total Files**: 30+
- **Total Content**: 1000+ hours learning material
- **Code Examples**: 70+
- **Practice Problems**: 200+
- **Documentation**: 5 main files

### Agent Size
- **Average Agent**: 3000-5000 words
- **Code Examples per Agent**: 10-15
- **Problem Count**: 20-40 per agent

### Skill Size
- **Average Skill**: 2000-3000 words
- **Code Examples per Skill**: 8-12
- **Tables/Matrices**: 3-5 per skill

## Extension Points

### Adding New Content

1. **New Agent**: Create `agents/XX-topic.md`
2. **New Skill**: Create `skills/XX-topic/SKILL.md`
3. **New Command**: Create `commands/new-command.md`
4. **New Hook**: Add to `hooks/hooks.json`

### Customization

- **Learning Paths**: Modify `/learn` command
- **Problem Sets**: Update skill problem recommendations
- **Assessment**: Customize `/assess` questions
- **Interview Prep**: Add company-specific tracks in `/interview-prep`

## Performance Considerations

### Load Strategy
- **Lazy Loading**: Skills load only when needed
- **Caching**: Agents cached after first load
- **Streaming**: Large content streamed to user

### Optimization
- **Minimal Redundancy**: Content organized hierarchically
- **Cross-linking**: Skills linked from agents, not duplicated
- **Index Structure**: Plugin.json serves as central index

## Integration Points

### With Claude Code
- **Agents**: Full agent system support
- **Skills**: SKILL.md format compatible
- **Commands**: Standard slash command system
- **Hooks**: Automation and tracking

### With External Services
- **LeetCode**: Problem links and references
- **GitHub**: Code examples and repositories
- **Visualization**: ASCII diagrams and tables
- **Assessment**: Test case validation

## Security & Validation

### Content Validation
- All code examples verified for correctness
- Complexity analysis double-checked
- Problem solutions tested

### User Data
- Progress tracking local only
- No external API calls
- Privacy-focused design

## Maintenance Guidelines

### Content Updates
- Keep agents focused and non-overlapping
- Update complexity analysis as needed
- Add new problem types when discovered

### Code Quality
- Consistent markdown formatting
- YAML frontmatter always present
- Code examples with comments

### Documentation
- Keep README updated
- Maintain ARCHITECTURE clarity
- Update LEARNING-PATH with new patterns

---

**This architecture ensures scalability, maintainability, and excellent user experience.**

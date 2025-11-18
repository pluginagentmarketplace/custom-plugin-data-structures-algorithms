# Data Structures & Algorithms Plugin - Style Guide

## Purpose

This guide ensures all plugin components maintain professional quality, consistency, and harmony. Every agent, skill, command, and hook follows these standards.

---

## Agent Standards

### Structure (Mandatory)
```
---
description: [Expert description, 1-2 sentences, mentions capabilities]
capabilities:
  - Capability 1
  - Capability 2
  - [5-8 total capabilities]
---

# Agent Title

## 🎯 Mission Statement
[1 paragraph mission, why this matters]

## 👨‍🏫 Expert Profile
- **Specialization**: [area]
- **Interview Coverage**: [percentage]
- **Real-world Impact**: [impact]
- **Difficulty**: [level]

## Overview
[2-3 paragraphs about what this agent covers]

## [Main Content Sections...]

## 📚 Resources & Links
[Link to related skills and commands]

## ✅ Mastery Checklist
[10-15 checkpoints for complete mastery]
```

### Content Requirements
1. **Descriptions**: Rich, specific, mention capabilities
2. **Mission Statements**: Compelling, motivating, clear purpose
3. **Expert Profiles**: Always include specialization, coverage, impact, difficulty
4. **Content**: At least 5 major sections
5. **Real-world Applications**: 2-3 case studies minimum
6. **Interview Prep**: Top questions and response framework
7. **Learning Progression**: Phased approach with checkpoints
8. **Common Mistakes**: 5-7 detailed mistakes to avoid
9. **Reference Tables**: Complexity, comparison matrices
10. **Mastery Checklist**: 10-15 clear checkpoints

### Tone
- Professional yet approachable
- Encouraging and empowering
- Clear and precise technical language
- Emoji for visual hierarchy (🎯 🎓 📚 🏆 ⚠️)
- Code examples in multiple languages when applicable

---

## Skill Standards (SKILL.md)

### Structure (Mandatory)
```yaml
---
name: skill-id  # Max 64 chars, lowercase, hyphens only
description: [Action-oriented, mentions when to use. Max 1024 chars]
---

# Skill Title

## Quick Start
[Immediate practical guidance, 30-50 words]

## [Core Sections...]

## [Practice/Examples]

## Key Insights
[5-7 bullet points]

## Next Steps
[Link to related skills or deeper learning]
```

### Requirements
1. **name**: Max 64 chars, lowercase, hyphens only
2. **description**: Max 1024 chars, action-oriented
3. **Quick Start**: First thing users see, immediate value
4. **Code Examples**: Working, tested, clear
5. **Practical Focus**: When to use, real-world applications
6. **Cross-references**: Link to other skills
7. **Progressive Complexity**: Simple → Advanced

### Quality Checklist
- [ ] Runs code examples tested
- [ ] YAML valid
- [ ] References correct
- [ ] Cross-links work
- [ ] No orphan skills
- [ ] Tone consistent
- [ ] Examples clear

---

## Command Standards (.md files)

### Structure
```
# /command-name

## Description
[Brief overview]

## How to Use
[Usage patterns]

## [Main Sections...]

## Examples
[Real usage examples]

## Tips
[Pro tips and best practices]

## Next Steps
[What to do after this command]
```

### Requirements
1. **Clear Purpose**: One sentence summary
2. **Usage Examples**: Show real usage
3. **Help Users Discover**: What comes next
4. **Interactive**: Guide users, don't just inform
5. **Reference Related**: Link to skills, agents, commands

---

## Hooks Standards (hooks.json)

### Structure
```json
{
  "hooks": {
    "hook_name": {
      "enabled": true,
      "description": "What this hook does",
      "triggers": [],
      "actions": []
    }
  },
  "analytics": {},
  "notifications": {},
  "adaptive_learning": {}
}
```

### Requirements
1. **Clear Descriptions**: Every hook documented
2. **Enabled by Default**: Good UX
3. **Trackable Events**: Proper metrics
4. **Non-intrusive**: Enhance, don't interfere
5. **Gamification**: Celebration, motivation
6. **Adaptive**: Learn from user behavior

---

## Documentation Standards

### README.md
- Professional marketing tone
- Clear section hierarchy
- Installation instructions
- Quick start examples
- Comprehensive feature list
- Real-world examples
- Call-to-action

### ARCHITECTURE.md
- Technical design
- Component relationships
- Data flow diagrams (text-based)
- Design patterns
- Extensibility points
- Performance considerations

### LEARNING_ROADMAP.md
- Week-by-week breakdown
- Daily schedules
- Progress checkpoints
- Success indicators
- Key problems
- Time estimates

### WORKFLOW.md
- How components connect
- Agent → Skill → Command → Hook flow
- User journey mapping
- Problem-solving workflows
- Integration patterns

---

## Writing Guidelines

### Tone
- **Professional**: Industry-standard terminology
- **Approachable**: Explain complex concepts clearly
- **Encouraging**: Motivate learners
- **Precise**: Technical accuracy paramount
- **Actionable**: Guide users to action

### Formatting
- **Headers**: Use 🎯 🎓 📚 🏆 emojis for visual hierarchy
- **Tables**: Compare options clearly
- **Code Blocks**: Syntax highlighting, tested examples
- **Lists**: Bullet for lists, numbers for steps
- **Emphasis**: Bold for key concepts, backticks for code

### Technical Accuracy
- [ ] All code examples tested
- [ ] Complexities correct
- [ ] References accurate
- [ ] Examples realistic
- [ ] Edge cases covered
- [ ] Cross-references valid

### Structure Quality
- [ ] Clear progression
- [ ] Logical sections
- [ ] Appropriate depth
- [ ] Examples provided
- [ ] No orphan content
- [ ] Proper linking

---

## Consistency Across Components

### Cross-Reference Requirements
1. **Agents** → List related Skills
2. **Skills** → Link related Skills
3. **Commands** → Reference Agents & Skills
4. **Hooks** → Track interaction with all

### Naming Conventions
- **Files**: Lowercase, hyphens, kebab-case
- **Sections**: Title Case for headers
- **Skills**: skill-id format (lowercase-hyphens)
- **Agents**: Number + topic format

### Metadata Standards
- **Descriptions**: Rich, specific, capability-listing
- **Keywords**: 5-10 searchable terms per component
- **Tags**: Consistent categorization
- **Links**: Always verify before publishing

---

## Quality Assurance Checklist

### Before Publishing
- [ ] Spelling and grammar correct
- [ ] Technical accuracy verified
- [ ] Code examples tested
- [ ] Links functional
- [ ] Tone consistent
- [ ] Structure logical
- [ ] Examples diverse
- [ ] Cross-references complete
- [ ] YAML valid (if applicable)
- [ ] Descriptions compelling

### Content Depth
- [ ] Beginner-friendly explanations
- [ ] Intermediate examples provided
- [ ] Advanced topics covered
- [ ] Real-world applications shown
- [ ] Edge cases addressed
- [ ] Common mistakes identified

### User Experience
- [ ] Clear entry points
- [ ] Natural progression
- [ ] Practical immediately useful
- [ ] Encouraging tone
- [ ] Success indicators clear
- [ ] Next steps obvious

---

## Component Harmony Framework

### Information Flow
```
Agent (What to learn)
    ↓
Skills (How to implement)
    ↓
Commands (What action to take)
    ↓
Hooks (How to celebrate progress)
```

### Integration Points
1. **Agent Description** → Lists related skills
2. **Skills** → Reference teaching agent
3. **Commands** → Invoke skills when needed
4. **Hooks** → Track all activity
5. **README** → Overview of all components

### Harmony Checklist
- [ ] Each agent has skills
- [ ] Each skill has clear use case
- [ ] Commands flow naturally
- [ ] Hooks don't break flow
- [ ] All pieces connect logically
- [ ] No dead ends
- [ ] Clear user journey

---

## Version Management

### Updating Guidelines
1. **Non-breaking changes**: Update directly
2. **Breaking changes**: Create new versions
3. **Deprecations**: Mark clearly with timeline
4. **Backwards compatibility**: Maintain when possible
5. **Changelogs**: Document all changes

### Release Quality
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Examples working
- [ ] No broken links
- [ ] Tone consistent
- [ ] Quality standards met

---

## Maintenance Standards

### Regular Reviews (Monthly)
- [ ] Check all links functional
- [ ] Verify code examples still work
- [ ] Update outdated information
- [ ] Review user feedback
- [ ] Enhance based on learner needs

### Quarterly Deep Dives
- [ ] Content freshness review
- [ ] Technology updates
- [ ] Industry best practices
- [ ] User success metrics
- [ ] Improvement planning

---

## Success Metrics

### Content Quality
- Learner satisfaction: ≥ 4.5/5
- Problem-solving success: ≥ 80%
- Interview preparation: ≥ 90% readiness
- Concept mastery: ≥ 85% completion

### User Experience
- Average time per agent: 4-6 hours
- Completion rate: ≥ 70%
- Skill building: ≥ 20 problems solved
- Knowledge retention: ≥ 80%

### System Health
- No broken links: 100%
- Code examples working: 100%
- Documentation complete: 100%
- Cross-references valid: 100%

---

## Contact & Feedback

For style guide questions or suggestions:
- Review this document
- Check existing examples
- Follow patterns consistently
- Ask for feedback before publishing

**Remember**: This style guide ensures professional, high-quality learning. Consistency across all components creates harmony and excellence.

---

*Last Updated: 2025-11-18*
*Version: 1.0*
*Status: Production Ready*

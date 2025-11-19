# 📥 Installation & Setup Guide

**Get DSA Mastery up and running in 5 minutes**

---

## System Requirements

- **Claude Code**: v1.0.0 or higher
- **Operating System**: macOS, Linux, Windows
- **Memory**: 100+ MB available
- **Internet**: Required for initial setup only

---

## Installation Methods

### Method 1: Claude Code GUI (Recommended)

1. **Open Claude Code**
   ```
   Launch Claude Code application
   ```

2. **Navigate to Settings**
   ```
   Settings → Plugins → Plugin Manager
   ```

3. **Add Plugin**
   ```
   "Add Plugin" button → Choose installation type
   ```

4. **Install from Local Directory**
   ```
   Select: "Custom Plugin Directory"
   Choose: custom-plugin-data-structures-algorithms folder
   Confirm: Install
   ```

5. **Verify Installation**
   ```
   /difficulty-selector  # Should respond with learning paths
   ```

---

### Method 2: Command Line

```bash
# Clone repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-data-structures-algorithms.git

# Navigate to directory
cd custom-plugin-data-structures-algorithms

# Install via Claude Code CLI (when available)
claude-code plugin install --path ./
```

---

### Method 3: Marketplace Installation (Future)

```bash
# When available in marketplace
/add-plugin dsa-mastery

# Or direct installation
/plugin install dsa-mastery
```

---

## Post-Installation Verification

### Test 1: Check Installation
```bash
/difficulty-selector
```
**Expected**: Shows three learning paths (Beginner, Intermediate, Advanced)

### Test 2: Browse Problems
```bash
/problem-solver
```
**Expected**: Lists 300+ problems by topic

### Test 3: Get Interview Prep
```bash
/interview-prep
```
**Expected**: Shows top 20 interview questions

### Test 4: Analyze Complexity
```bash
/complexity-analyzer
```
**Expected**: Shows Big O reference cards

---

## Quick Start (5 Minutes)

### Step 1: Choose Your Level (2 min)
```bash
/difficulty-selector
# Pick: Beginner (2 weeks), Intermediate (4 weeks), or Advanced (6 weeks)
```

### Step 2: Start with Problems (1 min)
```bash
/problem-solver
# Select: Your chosen difficulty level
# Browse: 100+ problems in that range
```

### Step 3: Learn Related Concepts (2 min)
```bash
# Each problem links to relevant skills
# Example: "Two Sum" → array-techniques skill
# Click to see code implementations and explanations
```

---

## Configuration

### Optional: Customize Hooks

Edit `hooks/hooks.json` for custom behavior:

```json
{
  "hooks": [
    {
      "name": "learning-progress-tracker",
      "enabled": true  // Set to false to disable
    }
  ]
}
```

---

## Troubleshooting

### Issue: Plugin Not Appearing

**Solution 1**: Verify file structure
```bash
ls .claude-plugin/plugin.json  # Should exist
```

**Solution 2**: Check plugin.json syntax
```bash
# Validate YAML format
cat .claude-plugin/plugin.json
```

**Solution 3**: Restart Claude Code
```
Close and reopen Claude Code application
```

---

### Issue: Commands Not Working

**Solution 1**: Verify commands directory
```bash
ls commands/
# Should show: problem-solver.md, difficulty-selector.md, etc.
```

**Solution 2**: Check markdown syntax
```
Commands must be valid markdown
No YAML frontmatter required for commands
```

---

### Issue: Skills Not Loading

**Solution 1**: Verify skills directory structure
```bash
ls -R skills/
# Should show domains: arrays/, trees/, graphs/, dp/, sorting/, hashing/, backtracking/, bitmanip/
```

**Solution 2**: Check YAML frontmatter in SKILL.md
```bash
# Each SKILL.md must have:
# ---
# name: skill-id
# description: description text
# ---
```

---

## Performance Optimization

### For Large Installations

1. **Enable Caching**
   ```
   Settings → Cache → Enable Plugin Cache
   ```

2. **Lazy Load Skills**
   ```
   Settings → Performance → Lazy Load Skills
   ```

3. **Limit Problem Set** (if needed)
   ```
   Edit commands/problem-solver.md to show top 100 only
   ```

---

## Uninstallation

### To Remove Plugin

```bash
# Via GUI
Settings → Plugins → DSA Mastery → Uninstall

# Via CLI
claude-code plugin uninstall dsa-mastery

# Or manually delete
rm -rf custom-plugin-data-structures-algorithms/
```

---

## Updates & Upgrades

### Check for Updates
```bash
git pull origin main
# or check GitHub for releases
```

### Update to Latest
```bash
cd custom-plugin-data-structures-algorithms
git pull
# Restart Claude Code
```

---

## Support & Help

### Get Help
- 📖 **Documentation**: See README.md for complete guide
- 🏗️ **Architecture**: See ARCHITECTURE.md for technical details
- 📋 **Issues**: Report bugs on GitHub
- 💬 **Community**: Share progress with others

---

## Next Steps

After successful installation:

1. ✅ Run `/difficulty-selector` to assess your level
2. ✅ Start with `/problem-solver` to find problems
3. ✅ Use `/complexity-analyzer` to understand Big O
4. ✅ Prepare for interviews with `/interview-prep`

---

**Installation complete! Now master DSA and land your dream job.** 🚀
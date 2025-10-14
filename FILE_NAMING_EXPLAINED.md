# Article File Naming System

## Overview

The agent now uses a two-file system: a working draft and timestamped final outputs.

## How It Works

### 1. Draft File (Work-in-Progress)

**Filename:** `article_draft.md`

**Purpose:** Track progress during execution

**Lifecycle:**
- Created after initial article generation (Step 4)
- Updated after video 2 refinement (Step 6)
- Updated after video 3 refinement (Step 7)
- **Overwritten on every workflow run**

**Use Case:** See the current state of the article as it's being built

---

### 2. Final File (Permanent)

**Filename:** `article_{topic}_{timestamp}.md`

**Example:** `article_context_engineering_20251014_103045.md`

**Purpose:** Permanent record of completed article

**Lifecycle:**
- Created at end of workflow (Step 9)
- **Never overwritten** - each run creates a new file
- Includes full cost metadata

**Use Case:** Historical record of all articles generated on each topic

---

## File Naming Rules

### Topic Name Cleaning
```python
# Original: "What is Context Engineering?"
# Cleaned: "what_is_context_engineering"

Rules:
- Lowercase
- Spaces → underscores
- Special characters → underscores
- Maximum 50 characters
```

### Timestamp Format
```python
Format: %Y%m%d_%H%M%S
Example: 20251014_103045
# Year-Month-Day_Hour-Minute-Second
```

## Example Workflow Run

### Topic: "context engineering"

```
STEP 4: Generate initial article
→ Saves: output/article_draft.md

STEP 6: Refine with video 2
→ Updates: output/article_draft.md

STEP 7: Refine with video 3
→ Updates: output/article_draft.md

STEP 9: Save final version
→ Creates: output/article_context_engineering_20251014_103045.md
```

## Repository Structure Over Time

```
output/
├── article_draft.md                                    # Always current draft
├── article_context_engineering_20251014_090030.md     # Oct 14, 9:00 AM
├── article_context_engineering_20251015_090045.md     # Oct 15, 9:00 AM
├── article_ai_trends_20251016_090100.md               # Oct 16, 9:00 AM (different topic)
└── article_context_engineering_20251017_090115.md     # Oct 17, 9:00 AM (same topic again)
```

## GitHub Actions Behavior

### What Gets Committed:
- ✅ `article_draft.md` (overwritten each run)
- ✅ `article_{topic}_{timestamp}.md` (new file each run)
- ✅ `logs/agent_log.txt` (updated each run)

### What Gets Uploaded as Artifact:
- ✅ All `article_*.md` files (both draft and final)
- ✅ `logs/agent_log.txt`

### Workflow Summary Shows:
- **Final Article:** `article_context_engineering_20251014_103045.md`
- **Word Count:** 2,450 words
- **Draft:** `article_draft.md` (overwritten each run)

## Benefits

### 1. Track Progress
See the draft file being updated in real-time during execution

### 2. Descriptive Filenames
Each final article includes:
- Topic name (easy to identify)
- Timestamp (when it was created)

### 3. Historical Record
All articles preserved:
- Compare different runs on the same topic
- Track improvements over time
- Never lose previous versions

### 4. Clean Organization
```
# Same topic, different days:
article_context_engineering_20251014.md
article_context_engineering_20251015.md
article_context_engineering_20251016.md

# Different topics, same day:
article_context_engineering_20251014_090030.md
article_ai_trends_20251014_150045.md
article_web3_20251014_210100.md
```

## Code Changes

### 1. Updated `save_article` Tool

**New Parameter:** `is_draft` (boolean)

```python
# Save draft
save_article({
    "article": current_article,
    "is_draft": True  # → article_draft.md
})

# Save final
save_article({
    "article": current_article,
    "is_draft": False  # → article_{topic}_{timestamp}.md
})
```

### 2. Updated `agent_direct.py`

**Draft Saves:**
- After step 4 (initial generation)
- After step 6 (video 2 refinement)
- After step 7 (video 3 refinement)

**Final Save:**
- After step 9 (with full metadata and costs)

### 3. Updated GitHub Workflow

**Commits:**
- All files in `output/` directory
- Includes both draft and final articles

**Summary:**
- Shows latest final article (not draft)
- Lists word count
- Notes that draft exists

## Examples

### Example 1: Single Run

**Input:** `topic.txt` contains "context engineering"

**Output Files:**
```
output/article_draft.md                         # Work-in-progress
output/article_context_engineering_20251014_103045.md  # Final
```

### Example 2: Multiple Runs, Same Topic

**Run 1 (Oct 14):**
```
output/article_draft.md                         # Overwritten
output/article_context_engineering_20251014_090030.md
```

**Run 2 (Oct 15):**
```
output/article_draft.md                         # Overwritten again
output/article_context_engineering_20251014_090030.md  # Still there
output/article_context_engineering_20251015_090045.md  # New!
```

### Example 3: Different Topics

**Run with "AI trends":**
```
output/article_draft.md                         # Overwritten
output/article_ai_trends_20251016_090100.md     # New topic!
```

## Searching for Articles

### Find All Articles for a Topic:
```bash
ls output/article_context_engineering_*.md
```

### Find Articles by Date:
```bash
ls output/article_*_20251014_*.md  # All articles on Oct 14
```

### View Latest Article:
```bash
ls -t output/article_*.md | grep -v draft | head -1
```

### Check Current Draft:
```bash
cat output/article_draft.md
```

## Git History

Each commit includes:
```
commit abc123
Date: Oct 14, 2025 9:00 AM
Message: Auto-generated article: 2025-10-14-0900

Changes:
  modified: output/article_draft.md
  added:    output/article_context_engineering_20251014_090030.md
  modified: logs/agent_log.txt
```

You can see:
- When each article was generated
- What topic it was about
- How the draft evolved

## Migration from Old System

**Old System:**
- Single timestamped file: `article_20251014_103045.md`
- No topic name in filename
- No work-in-progress tracking

**New System:**
- Draft file: `article_draft.md` (work-in-progress)
- Final file: `article_{topic}_{timestamp}.md` (descriptive + timestamped)
- Better organization and searchability

## Summary

✅ **Draft file:** Shows progress during execution, overwritten each run
✅ **Final files:** Permanent record with topic + timestamp
✅ **GitHub commits:** All files preserved in history
✅ **Easy search:** Find articles by topic or date
✅ **Clear organization:** Know what each file is at a glance

---

**Updated:** 2025-10-14

# Tool API Reference

Complete reference for all tool interfaces in the YouTube Article Agent.

---

## Tool 1: `read_input_files`

**Description:** Read the topic and article prompt from input files (topic.txt and article_prompt.txt)

**Parameters:** None

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Successfully read input files:\n\nTopic: {topic}\n\nArticle Prompt Length: {length} characters"
    }],
    "topic": str,              # The search topic
    "article_prompt": str      # Article writing instructions
}
```

**Error Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Error: {error_message}"
    }],
    "isError": True
}
```

**Example Usage:**
```python
result = read_input_files({})
topic = result["topic"]
article_prompt = result["article_prompt"]
```

---

## Tool 2: `search_youtube`

**Description:** Search YouTube for videos on a given topic and return top 3 videos sorted by engagement (comments, then views)

**Parameters:**
```python
{
    "topic": str  # The search query/topic
}
```

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Found {count} videos with captions for topic: '{topic}'\n\nTop 3 videos by engagement:..."
    }],
    "videos": [
        {
            "video_id": str,        # YouTube video ID (e.g., "dQw4w9WgXcQ")
            "title": str,           # Video title
            "channel": str,         # Channel name
            "description": str,     # Video description
            "published_at": str,    # ISO 8601 timestamp
            "views": int,           # View count
            "comments": int,        # Comment count
            "likes": int,           # Like count
            "duration": str         # ISO 8601 duration (e.g., "PT5M30S")
        },
        # ... up to 3 videos
    ],
    "success": True
}
```

**Error Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "YouTube API Error: {reason}"
    }],
    "isError": True
}
```

**Example Usage:**
```python
result = search_youtube({"topic": "python tutorials"})
if result.get("success"):
    videos = result["videos"]
    for video in videos:
        video_id = video["video_id"]
        title = video["title"]
```

---

## Tool 3: `get_transcript`

**Description:** Extract English transcript from a YouTube video by video ID

**Parameters:**
```python
{
    "video_id": str,      # YouTube video ID
    "video_title": str    # Title of the video (for logging)
}
```

**Returns (Success):**
```python
{
    "content": [{
        "type": "text",
        "text": "Successfully extracted transcript for: {video_title}\n\nVideo ID: {video_id}\nTranscript length: {length} characters\nWord count: ~{count} words"
    }],
    "video_id": str,       # The video ID
    "transcript": str,     # Full transcript text (cleaned)
    "word_count": int,     # Approximate word count
    "success": True
}
```

**Returns (Failure):**
```python
{
    "content": [{
        "type": "text",
        "text": "No English transcript found for video: {video_title} (ID: {video_id})\n\nThis video may not have captions available. Skipping..."
    }],
    "video_id": str,
    "success": False,
    "error": str          # Error description
}
```

**Possible Errors:**
- "Transcripts disabled"
- "No transcript found"
- "Video unavailable"

**Example Usage:**
```python
result = get_transcript({
    "video_id": "dQw4w9WgXcQ",
    "video_title": "Example Video"
})

if result.get("success"):
    transcript = result["transcript"]
    word_count = result["word_count"]
else:
    # Skip to next video
    pass
```

---

## Tool 4: `generate_initial_article`

**Description:** Generate the first draft of an article from a YouTube video transcript

**Parameters:**
```python
{
    "transcript": str,        # The video transcript text
    "article_prompt": str,    # User's article writing instructions
    "video_title": str,       # Title of the video
    "channel_name": str,      # Name of the channel
    "topic": str              # Original search topic
}
```

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Successfully generated initial article draft!\n\nSource: {video_title}\nArticle length: {length} characters\nWord count: ~{count} words\n\n💰 Cost: ${cost:.4f} (Input: {in_tokens:,} tokens, Output: {out_tokens:,} tokens)"
    }],
    "article": str,           # Generated article in markdown format
    "word_count": int,        # Word count of article
    "input_tokens": int,      # Claude API input tokens used
    "output_tokens": int,     # Claude API output tokens used
    "cost": float,            # Cost of this API call in USD
    "success": True
}
```

**Error Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Error generating article: {error}"
    }],
    "isError": True,
    "success": False
}
```

**Example Usage:**
```python
result = generate_initial_article({
    "transcript": "Hello world...",
    "article_prompt": "Write in conversational tone...",
    "video_title": "Python Tutorial",
    "channel_name": "Tech Channel",
    "topic": "python basics"
})

if result.get("success"):
    article = result["article"]
    cost = result["cost"]
    input_tokens = result["input_tokens"]
    output_tokens = result["output_tokens"]
```

**Cost Information:**
- Model: Claude Sonnet 4.0 (claude-sonnet-4-0-20250514)
- Input: $3.00 per 1M tokens
- Output: $15.00 per 1M tokens
- Typical cost: $0.05-0.15 per article

---

## Tool 5: `refine_article`

**Description:** Refine and improve the article by incorporating insights from additional video transcripts

**Parameters:**
```python
{
    "current_article": str,   # The current article draft
    "new_transcript": str,    # Transcript from the new video
    "article_prompt": str,    # User's article writing instructions
    "video_title": str,       # Title of the new video
    "channel_name": str,      # Channel of the new video
    "iteration": int          # Which iteration (2 or 3)
}
```

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Successfully refined article with insights from Video {iteration}!\n\nNew source: {video_title}\nRefined article length: {length} characters\nWord count: ~{count} words\n\n💰 Cost: ${cost:.4f} (Input: {in_tokens:,} tokens, Output: {out_tokens:,} tokens)"
    }],
    "article": str,           # Refined article in markdown format
    "word_count": int,        # Word count of refined article
    "input_tokens": int,      # Claude API input tokens used
    "output_tokens": int,     # Claude API output tokens used
    "cost": float,            # Cost of this API call in USD
    "success": True
}
```

**Error Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Error refining article: {error}"
    }],
    "isError": True,
    "success": False
}
```

**Example Usage:**
```python
result = refine_article({
    "current_article": "# My Article\n\n...",
    "new_transcript": "Additional insights...",
    "article_prompt": "Write in conversational tone...",
    "video_title": "Advanced Python",
    "channel_name": "Tech Channel",
    "iteration": 2
})

if result.get("success"):
    refined_article = result["article"]
    cost = result["cost"]
```

---

## Tool 6: `save_article`

**Description:** Save the final article to output/article.md with metadata including cost information

**Parameters:**
```python
{
    "article": str,              # The article content in markdown
    "video_sources": list,       # List of video metadata dicts
    "topic": str,                # The original search topic
    "total_cost": float,         # Total cost of all API calls
    "total_input_tokens": int,   # Total input tokens used
    "total_output_tokens": int   # Total output tokens used
}
```

**video_sources structure:**
```python
[
    {
        "video_id": str,
        "title": str,
        "channel": str,
        "views": int,
        "comments": int
    },
    # ... more videos
]
```

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Article successfully saved to: {path}\n\nTotal length: {length} characters\nSources included: {count} videos"
    }],
    "file_path": str,     # Absolute path to saved file
    "success": True
}
```

**Error Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Error: Missing required field '{field}' in save_article call"
    }],
    "isError": True,
    "success": False
}
```

**Validation Rules:**
- `article` must not be empty
- `video_sources` must be a list (can be empty but will show warning)
- `topic` is required
- Cost fields are optional (default to 0)

**Example Usage:**
```python
result = save_article({
    "article": "# My Article\n\n...",
    "video_sources": [
        {
            "video_id": "abc123",
            "title": "Python Tutorial",
            "channel": "Tech Channel",
            "views": 10000,
            "comments": 500
        }
    ],
    "topic": "python basics",
    "total_cost": 0.15,
    "total_input_tokens": 5000,
    "total_output_tokens": 3000
})

if result.get("success"):
    file_path = result["file_path"]
```

---

## Tool 7: `track_cost`

**Description:** Track cumulative cost of Claude API calls

**Parameters:**
```python
{
    "input_tokens": int,   # Number of input tokens used
    "output_tokens": int,  # Number of output tokens used
    "cost": float,         # Cost of this API call in USD
    "operation": str       # Description of the operation
}
```

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": "Cost tracked for {operation}: ${cost:.4f}\n\nRunning total: ${total:.4f} ({calls} API calls)"
    }],
    "success": True
}
```

**Example Usage:**
```python
track_cost({
    "input_tokens": 1500,
    "output_tokens": 2000,
    "cost": 0.0345,
    "operation": "Initial article generation"
})
```

**Note:** Uses global state to accumulate costs across multiple calls

---

## Tool 8: `get_total_cost`

**Description:** Get the total accumulated cost of all Claude API calls

**Parameters:** None

**Returns:**
```python
{
    "content": [{
        "type": "text",
        "text": """
╔════════════════════════════════════════════╗
║         COST SUMMARY - FINAL REPORT        ║
╚════════════════════════════════════════════╝

📊 API Usage Statistics:
   • Total API Calls: {calls}
   • Input Tokens: {in_tokens:,}
   • Output Tokens: {out_tokens:,}
   • Total Tokens: {total_tokens:,}

💰 Cost Breakdown:
   • Input Cost:  ${in_cost:.4f} (@$3/M tokens)
   • Output Cost: ${out_cost:.4f} (@$15/M tokens)

💵 TOTAL COST: ${total:.4f}

Model: Claude Sonnet 4.0 (claude-sonnet-4-0-20250514)
"""
    }],
    "total_cost": float,           # Total cost in USD
    "total_input_tokens": int,     # Total input tokens across all calls
    "total_output_tokens": int,    # Total output tokens across all calls
    "api_calls": int,              # Number of API calls made
    "success": True
}
```

**Example Usage:**
```python
result = get_total_cost({})
total_cost = result["total_cost"]
total_input_tokens = result["total_input_tokens"]
total_output_tokens = result["total_output_tokens"]
```

---

## Data Flow Example

Complete workflow showing how to chain tools together:

```python
# Step 1: Read inputs
inputs = read_input_files({})
topic = inputs["topic"]
article_prompt = inputs["article_prompt"]

# Step 2: Search YouTube
search_result = search_youtube({"topic": topic})
videos = search_result["videos"]

# Step 3: Get transcript
transcript_result = get_transcript({
    "video_id": videos[0]["video_id"],
    "video_title": videos[0]["title"]
})

if transcript_result["success"]:
    # Step 4: Generate article
    gen_result = generate_initial_article({
        "transcript": transcript_result["transcript"],
        "article_prompt": article_prompt,
        "video_title": videos[0]["title"],
        "channel_name": videos[0]["channel"],
        "topic": topic
    })

    # Step 5: Track cost
    track_cost({
        "input_tokens": gen_result["input_tokens"],
        "output_tokens": gen_result["output_tokens"],
        "cost": gen_result["cost"],
        "operation": "Initial article generation"
    })

    # Step 6: Get total cost
    cost_summary = get_total_cost({})

    # Step 7: Save article
    save_article({
        "article": gen_result["article"],
        "video_sources": [videos[0]],
        "topic": topic,
        "total_cost": cost_summary["total_cost"],
        "total_input_tokens": cost_summary["total_input_tokens"],
        "total_output_tokens": cost_summary["total_output_tokens"]
    })
```

---

## Error Handling Best Practices

1. **Always check `success` field** before accessing data fields
2. **Handle `isError` returns** gracefully
3. **Skip failed transcript extractions** and continue to next video
4. **Validate data types** before passing to next tool
5. **Log errors** for debugging

---

## Common Patterns

### Pattern 1: Safe Data Extraction
```python
result = some_tool({...})

# Safe way
if result.get("success"):
    data = result["field_name"]
else:
    # Handle error
    error = result.get("error", "Unknown error")
```

### Pattern 2: Looping Through Videos
```python
videos = search_result["videos"]
successful_transcripts = []

for video in videos[:3]:  # Top 3 only
    transcript_result = get_transcript({
        "video_id": video["video_id"],
        "video_title": video["title"]
    })

    if transcript_result.get("success"):
        successful_transcripts.append({
            "video": video,
            "transcript": transcript_result["transcript"]
        })
```

### Pattern 3: Building video_sources List
```python
video_sources = []
for item in successful_transcripts:
    video_sources.append({
        "video_id": item["video"]["video_id"],
        "title": item["video"]["title"],
        "channel": item["video"]["channel"],
        "views": item["video"]["views"],
        "comments": item["video"]["comments"]
    })
```

---

**Last Updated:** 2025-10-13
